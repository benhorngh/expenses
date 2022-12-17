from dotenv import dotenv_values
from pydantic import BaseModel

from database.dummy_db import DummyDB
from expenses_server.database.expenses_db import ExpensesDB


class Settings(BaseModel):
    # data files
    cal_file_path: str
    max_file_path: str
    leumi_file_path: str
    pepper_file_path: str

    # moneylover
    wallet_name: str
    auth_token: str

    # dummy db
    db_type: str
    transactions_file: str
    rules_file: str


class Globals(BaseModel):
    transaction_db: ExpensesDB
    rules_db: ExpensesDB

    class Config:
        arbitrary_types_allowed = True


class AppSettings:
    settings: Settings = None
    globals: Globals = None


def init_settings():
    values = dotenv_values()
    AppSettings.settings = Settings(max_file_path=values['MAX_FILE_NAME'],
                                    cal_file_path=values['CAL_FILE_NAME'],
                                    leumi_file_path=values['LEUMI_FILE_NAME'],
                                    pepper_file_path=values['PEPPER_FILE_NAME'],
                                    wallet_name=values['WALLET_NAME'],
                                    auth_token=values['AUTH_TOKEN'],
                                    transactions_file=values['TRANSACTIONS_FILE'],
                                    rules_file=values['RULES_FILE'],
                                    db_type=values['DB_TYPE']
                                    )
    init_globals()


def init_globals():
    if AppSettings.settings.db_type == 'dummy':
        AppSettings.globals = Globals(transaction_db=DummyDB(filename=AppSettings.settings.transactions_file),
                                      rules_db=DummyDB(filename=AppSettings.settings.rules_file))
