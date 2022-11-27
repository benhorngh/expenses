import abc

import pandas as pd


class ExpensesDB(abc.ABC):
    """Abstract DAL"""

    def store_all_transaction(self, transactions: pd.DataFrame) -> None:
        raise NotImplementedError()

    def get_all_transaction(self) -> pd.DataFrame:
        raise NotImplementedError()

    def load_data(self) -> None:
        raise NotImplementedError()

    def is_db_exist(self) -> None:
        raise NotImplementedError()
