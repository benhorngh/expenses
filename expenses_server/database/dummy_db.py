import os

import numpy as np
import pandas as pd

from expenses_server.common.models import C
from expenses_server.database.expenses_db import ExpensesDB

FILE_NAME = os.path.join("data_files", 'transactions_db.csv')


class DummyDB(ExpensesDB):
    _TRANSACTIONS = None

    def store_all_transaction(self, transactions: pd.DataFrame) -> None:
        DummyDB._TRANSACTIONS = transactions
        transactions.to_csv(FILE_NAME, index=False)

    def get_all_transaction(self) -> pd.DataFrame:
        return DummyDB._TRANSACTIONS

    def load_data(self):
        data = pd.read_csv(FILE_NAME, parse_dates=[C.T_DATE])
        data = data.replace({np.nan: None})
        DummyDB._TRANSACTIONS = data
