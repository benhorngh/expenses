import pandas as pd

from expenses_server.database.expenses_db import ExpensesDB


class DummyDB(ExpensesDB):
    _TRANSACTIONS = None

    def store_all_transaction(self, transactions: pd.DataFrame) -> None:
        DummyDB._TRANSACTIONS = transactions

    def get_all_transaction(self) -> pd.DataFrame:
        return DummyDB._TRANSACTIONS

