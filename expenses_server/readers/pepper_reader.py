from datetime import datetime

import pandas as pd

from expenses_server.common.models import Transaction, C, TransactionType
from expenses_server.readers.abstract_read_data import AbstractDataReader, OverrideColumn


class PepperReader(AbstractDataReader):
    """
    Export pepper pdf of transactions,
    Then open using pdf adobe reader,
    And export as .txt
    """

    def __init__(self, file_path: str, **kwargs):
        override_by_class = [OverrideColumn(column_name=C.T_TYPE, value=TransactionType.BANK)]
        super().__init__(file_path, override_by_class=override_by_class, **kwargs)

    def read_file(self) -> pd.DataFrame:
        return pd.DataFrame(data=read_pepper(self._file_path))

    def convert_row_to_transaction(self, row) -> Transaction:
        return Transaction(t_date=row['date'],
                           business=row['description'] or '',
                           money=row['money'],
                           )


def _remove_non_relevant_paragraphs(text: str):
    paragraphs = text.split('\n\n\n')
    tables = paragraphs[6:-1]
    tables.pop(1)
    tables_text = '\n'.join(tables)
    return tables_text


def _is_row_date(row: str):
    return len(row.split('.')) == 3 and row.split('.')[0].isnumeric()


def _row_to_date(row: str):
    return datetime.strptime(row, '%d.%m.%Y')


def _is_row_transaction_id(row: str):
    return row.startswith('FT')


def _row_to_number(row: str):
    return float(row.replace(',', ''))


def _is_row_money_value(row: str):
    return '.' in row and len(row.split('.')) == 2 and row.split('.')[1].isnumeric()


def read_pepper(filename: str):
    with open(filename, encoding="utf8") as p:
        text = p.read()
        tables_text = _remove_non_relevant_paragraphs(text)
        rows = tables_text.split('\n')
        try_again_indexes = []
        data = []
        for index, row in enumerate(rows):
            if _is_row_date(row):
                money, description = None, None
                t_date = _row_to_date(row)
                t_money_start = index + 2
                if not _is_row_transaction_id(rows[index + 1]):
                    description = rows[index + 1]
                    t_money_start += 1
                try:
                    money = _row_to_number(rows[t_money_start]) - _row_to_number(rows[t_money_start + 1])
                    data.append({'date': t_date, 'description': description, 'money': money})
                except:
                    try_again_indexes += [index]

        failed_indexes = []
        for index in try_again_indexes:
            t_date = _row_to_date(rows[index])
            money_values = [_row_to_number(row) for row in rows[index: index + 15] if _is_row_money_value(row)]
            if len(money_values) >= 2:
                data.append({'date': t_date, 'description': '', 'money': money_values[0] - money_values[1]})
            else:
                failed_indexes += [index]
        if failed_indexes:
            raise NotImplementedError(f"Couldn't read all transactions. rows {failed_indexes}")
    return data
