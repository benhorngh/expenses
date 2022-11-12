import pandas as pd

from expenses_server.common.models import C
from expenses_server.readers.cal_reader import CalReader
from expenses_server.readers.leumi_reader import LeumiReader
from expenses_server.readers.max_foreign_curr_reader import MaxForeignCurrencyReader
from expenses_server.readers.max_reader import MaxReader
from expenses_server.common.settings import AppSettings


def read_all_data():
    data_files = AppSettings.settings.data_files
    cal = CalReader(data_files.cal_file_path).start()
    max_cards = MaxReader(data_files.max_file_path).start()
    max_foreign_cards = MaxForeignCurrencyReader(data_files.max_file_path).start()
    leumi = LeumiReader(data_files.leumi_file_path).start()

    return pd.concat([cal, max_cards, max_foreign_cards, leumi])


def generate_transaction_id(row):
    date_str = row[C.T_DATE].date().isoformat()
    money_str = str(abs(row[C.MONEY])).replace(".", "-")
    business_str = '-'.join([str(ord(c)) for c in row[C.BUSINESS].replace(" ", "-")[:3]])
    return f't_{date_str}_{money_str}_{business_str}'


def init_db(override: bool):
    if override:
        data = read_all_data()
        data[C.T_ID] = data.apply(generate_transaction_id, axis=1)
        AppSettings.settings.db_instance.store_all_transaction(data)
    AppSettings.settings.db_instance.load_data()
