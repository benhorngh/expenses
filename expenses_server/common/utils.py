import pandas as pd

from expenses_server.common.models import C, SpecialTypeId, TransactionCategory
from expenses_server.readers.cal_reader import CalReader
from expenses_server.readers.leumi_reader import LeumiReader
from expenses_server.readers.max_foreign_curr_reader import MaxForeignCurrencyReader
from expenses_server.readers.max_reader import MaxReader
from expenses_server.common.settings import AppSettings
from readers.abstract_read_data import OverrideColumn
from readers.pepper_reader import PepperReader
from services import categorize_service
from services.categorize_service import Rule, RuleType


def read_all_data():
    cal = CalReader(AppSettings.settings.cal_file_path,
                    custom_override=[OverrideColumn(column_name=C.TYPE_ID, value=SpecialTypeId.CREDIT_CARD_CAL)]
                    ).start()
    max_cards = MaxReader(AppSettings.settings.max_file_path).start()
    max_foreign_cards = MaxForeignCurrencyReader(AppSettings.settings.max_file_path).start()
    leumi = LeumiReader(AppSettings.settings.leumi_file_path,
                        custom_override=[OverrideColumn(column_name=C.TYPE_ID, value=SpecialTypeId.BANK_LEUMI)]
                        ).start()
    pepper = PepperReader(AppSettings.settings.pepper_file_path,
                          custom_override=[OverrideColumn(column_name=C.TYPE_ID, value=SpecialTypeId.BANK_PEPPER)]
                          ).start()

    return pd.concat([cal, max_cards, max_foreign_cards, leumi, pepper])


def generate_transaction_id(row):
    date_str = row[C.T_DATE].date().isoformat()
    money_str = str(abs(row[C.MONEY])).replace(".", "-")
    business_str = '-'.join([str(ord(c)) for c in row[C.BUSINESS].replace(" ", "-")[:3]])
    return f't_{date_str}_{money_str}_{business_str}'


def init_db():
    if not AppSettings.globals.rules_db.is_db_exist():
        placeholder = Rule(r_type=RuleType.transaction_id, value="empty", category=TransactionCategory.UNKNOWN_EXPENSE)
        rules_data = pd.DataFrame(data=[placeholder.dict()])
        AppSettings.globals.rules_db.store_all_data(rules_data)
    AppSettings.globals.rules_db.load_data()

    if not AppSettings.globals.transaction_db.is_db_exist():
        data = read_all_data()
        data[C.T_ID] = data.apply(generate_transaction_id, axis=1)
        categorize_service.apply_rules(data)
        AppSettings.globals.transaction_db.store_all_data(data)
    AppSettings.globals.transaction_db.load_data([C.T_DATE])


