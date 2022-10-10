from dotenv import dotenv_values
from pydantic import BaseModel

from expenses_server.database.expenses_db import ExpensesDB


class DataFiles(BaseModel):
    cal_file_path: str
    max_file_path: str
    leumi_file_path: str


class Settings(BaseModel):
    db_instance: ExpensesDB
    data_files: DataFiles

    class Config:
        arbitrary_types_allowed = True


class AppSettings:
    settings: Settings = None


def init_settings(db_instance: ExpensesDB):
    values = dotenv_values()
    data_files = DataFiles(max_file_path=values['MAX_FILE_NAME'],
                           cal_file_path=values['CAL_FILE_NAME'],
                           leumi_file_path=values['LEUMI_FILE_NAME']
                           )
    AppSettings.settings = Settings(db_instance=db_instance, data_files=data_files)
