import abc

import pandas as pd


class ExpensesDB(abc.ABC):
    """Abstract DAL"""

    def store_all_transaction(self, transactions: pd.DataFrame) -> None:
        raise NotImplementedError()

    def get_all_transaction(self) -> pd.DataFrame:
        raise NotImplementedError()

