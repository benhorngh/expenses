import math
from datetime import datetime
from typing import List, Optional

import pandas as pd

from expenses_server.common.models import Transaction, TransactionType, C
from expenses_server.readers.abstract_read_data import AbstractDataReader, OverrideColumn


class MaxForeignCurrencyReader(AbstractDataReader):
    """
    Max reader - foreign currency (Dollar, Euro, etc)
    """

    def __init__(self, file_path: str, **kwargs):
        override_by_class = [OverrideColumn(column_name=C.T_TYPE, value=TransactionType.CARD)]
        super().__init__(file_path, override_by_class=override_by_class, **kwargs)

    def read_file(self) -> pd.DataFrame:
        xl_file = pd.ExcelFile(self._file_path)
        return pd.read_excel(xl_file, 1, skiprows=[0, 1, 2])

    def convert_row_to_transaction(self, row) -> Optional[Transaction]:
        def get_max_t_date(date_s: str) -> datetime:
            date_arr = [int(v) for v in date_s.split("-")]
            return datetime(year=date_arr[2], month=date_arr[1], day=date_arr[0])

        def get_card_name(card):
            if card:
                if isinstance(card, float):
                    return str(int(card))
            return card

        money = row.get("סכום חיוב")
        if not money or math.isnan(money):
            return None
        return Transaction(t_date=get_max_t_date(row.get("תאריך עסקה")),
                           business=row.get("שם בית העסק"),
                           type_id=get_card_name(row.get("4 ספרות אחרונות של כרטיס האשראי")),
                           money=money * -1)
