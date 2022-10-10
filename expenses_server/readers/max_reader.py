from datetime import datetime

import pandas as pd

from expenses_server.common.models import Transaction, TransactionType
from expenses_server.readers.abstract_read_data import AbstractDataReader


class MaxReader(AbstractDataReader):

    def __init__(self, file_path: str):
        super().__init__(file_path, TransactionType.CARD)

    def read_file(self) -> pd.DataFrame:
        return pd.read_excel(self._file_path, skiprows=[0, 1, 2])

    def convert_row_to_transaction(self, row) -> Transaction:
        def get_max_t_date(date_s: str) -> datetime:
            date_arr = [int(v) for v in date_s.split("-")]
            return datetime(year=date_arr[2], month=date_arr[1], day=date_arr[0])

        return Transaction(t_date=get_max_t_date(row.get("תאריך עסקה")),
                           business=row.get("שם בית העסק"),
                           card=row.get("4 ספרות אחרונות של כרטיס האשראי"),
                           money=row.get("סכום חיוב") * -1)
