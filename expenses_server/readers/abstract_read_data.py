from typing import List, Any

import pandas as pd
from pydantic import BaseModel

from expenses_server.common.models import Transaction


class OverrideColumn(BaseModel):
    column_name: str
    value: Any


class AbstractDataReader:
    def __init__(self, file_path: str,
                 override_by_class: List[OverrideColumn] = None,
                 custom_override: List[OverrideColumn] = None):
        self._file_path = file_path
        self._override = (override_by_class or []) + (custom_override or [])

    def start(self) -> pd.DataFrame:
        raw = self.read_file()
        transactions = [self.convert_row_to_transaction(row) for row in raw.to_dict(orient="index").values()]
        transactions = [t.dict() for t in transactions if t]
        processed = pd.DataFrame(data=transactions)
        for override in self._override:
            processed[override.column_name] = override.value
        return processed

    def read_file(self) -> pd.DataFrame:
        raise NotImplemented()

    def convert_row_to_transaction(self, row) -> Transaction:
        raise NotImplemented()
