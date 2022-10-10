import re
from datetime import datetime
from typing import Union

import pandas as pd

from expenses_server.common.models import Transaction, TransactionType
from expenses_server.readers.abstract_read_data import AbstractDataReader


class CalReader(AbstractDataReader):

    def __init__(self, file_path: str):
        super().__init__(file_path, TransactionType.CARD)

    def read_file(self) -> pd.DataFrame:
        return pd.read_excel(self._file_path, skiprows=[0, 1], skipfooter=1)

    def convert_row_to_transaction(self, row) -> Transaction:
        def get_cal_t_date(date_s: Union[str, datetime]) -> datetime:
            if isinstance(date_s, str):
                date_arr = [int(v) for v in date_s.split("/")]
                if len(str(date_arr[2])) == 2:
                    date_arr[2] += 2000
                return datetime(year=date_arr[2], month=date_arr[1], day=date_arr[0])
            else:
                return date_s

        def get_bus_name(bus_name: str):
            if bus_name and isinstance(bus_name, str):
                reg = re.compile(r'^[A-Za-z ]*$')
                if reg.match(bus_name):
                    return bus_name[::-1]
            return bus_name

        return Transaction(t_date=get_cal_t_date(row.get("תאריך העסקה")),
                           business=get_bus_name(row.get("שם בית העסק")),
                           card=row.get("4 ספרות אחרונות של כרטיס האשראי"),
                           money=float(row.get("סכום החיוב")[2:]) * -1)
