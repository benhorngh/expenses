from common.models import SpecialTypeId
from expenses_server.common import settings, utils
from expenses_server.common.settings import AppSettings
from expenses_server.database.dummy_db import DummyDB
from services import data_manipulation, records_service, money_lover


def init_settings():
    settings.init_settings(db_instance=DummyDB())


def init_data():
    utils.init_db()


if __name__ == "__main__":
    init_settings()
    init_data()

    data = AppSettings.settings.db_instance.get_all_transaction()
    data_manipulation.prepare_date(data)
    data_manipulation.add_missing_category(data)
    relevant_data = data_manipulation.get_by_type_id(data, [SpecialTypeId.BANK_LEUMI])
    transactions = records_service.convert_to_transactions(relevant_data)
    money_lover.send_to_money_lover(transactions,
                                    AppSettings.settings.money_lover.wallet_name,
                                    AppSettings.settings.money_lover.auth_token)
