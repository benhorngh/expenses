import pandas as pd

from expenses_server.common.models import Transaction, TransactionType, C


class AbstractDataReader:
    def __init__(self, file_path: str, t_type: TransactionType = None):
        self._file_path = file_path
        self.t_type = t_type

    def start(self) -> pd.DataFrame:
        raw = self.read_file()
        transactions = [self.convert_row_to_transaction(row).dict() for row in raw.to_dict(orient="index").values()]
        processed = pd.DataFrame(data=transactions)
        processed[C.T_TYPE] = self.t_type
        return processed

    def read_file(self) -> pd.DataFrame:
        raise NotImplemented()

    def convert_row_to_transaction(self, row) -> Transaction:
        raise NotImplemented()
