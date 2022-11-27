import re
from datetime import datetime
from typing import Union

import pandas as pd

from expenses_server.common.models import Transaction, TransactionType, C
from expenses_server.readers.abstract_read_data import AbstractDataReader, OverrideColumn


class CalReader(AbstractDataReader):
    """
    Export cal transaction excel,
    Then upload to Google Sheets and download as .csv file
    """

    def __init__(self, file_path: str, **kwargs):
        override_by_class = [OverrideColumn(column_name=C.T_TYPE, value=TransactionType.CARD)]
        super().__init__(file_path, override_by_class=override_by_class, **kwargs)

    def read_file(self) -> pd.DataFrame:
        return pd.read_csv(self._file_path, skiprows=[0, 1], skipfooter=1, engine='python')

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
                           type_id=str(row.get("4 ספרות אחרונות של כרטיס האשראי")),
                           money=float(row.get("סכום החיוב")[2:]) * -1,)
