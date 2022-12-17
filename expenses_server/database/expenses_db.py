import abc

import pandas as pd


class ExpensesDB(abc.ABC):
    """Abstract DAL"""

    def store_all_data(self, transactions: pd.DataFrame) -> None:
        raise NotImplementedError()

    def get_all_data(self) -> pd.DataFrame:
        raise NotImplementedError()

    def load_data(self, *args, **kwargs) -> None:
        raise NotImplementedError()

    def is_db_exist(self) -> None:
        raise NotImplementedError()
