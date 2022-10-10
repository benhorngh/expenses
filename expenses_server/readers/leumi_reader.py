from datetime import datetime

import pandas as pd

from expenses_server.common.models import Transaction, TransactionType
from expenses_server.readers.abstract_read_data import AbstractDataReader


class LeumiReader(AbstractDataReader):

    def __init__(self, file_path: str):
        super().__init__(file_path, TransactionType.BANK)

    def read_file(self) -> pd.DataFrame:
        return pd.read_html(self._file_path, skiprows=[0, 1])[1]

    def convert_row_to_transaction(self, row) -> Transaction:
        def get_t_date(date_s: str) -> datetime:
            date_arr = [int(v) for v in date_s.split("/")]
            return datetime(year=2000 + date_arr[2], month=date_arr[1], day=date_arr[0])

        return Transaction(t_date=get_t_date(row.get(0)),
                           business=row.get(2),
                           money=(row.get(4) * -1) + row.get(5),
                           t_id=(row.get(3)))


if __name__ == '__main__':
    transactions = LeumiReader('leumi.xls').start()
    print(transactions)
