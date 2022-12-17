import os
from typing import List

import numpy as np
import pandas as pd

from expenses_server.database.expenses_db import ExpensesDB


class DummyDB(ExpensesDB):

    def __init__(self, filename: str):
        self.data = None
        self.filename = filename

    def store_all_data(self, data: pd.DataFrame) -> None:
        self.data = data
        data.to_csv(self.filename, index=False)

    def get_all_data(self) -> pd.DataFrame:
        return self.data

    def load_data(self, parse_dates: List[str] = None):
        data = pd.read_csv(self.filename, parse_dates=parse_dates)
        data = data.replace({np.nan: None})
        self.data = data

    def is_db_exist(self):
        return os.path.isfile(self.filename)
