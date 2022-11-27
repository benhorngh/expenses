from expenses_server.common.models import TransactionCategory
from expenses_server.common.settings import AppSettings
from expenses_server.services import data_manipulation


def categorize_by_business_name(category: TransactionCategory, business_name: str):
    data = AppSettings.settings.db_instance.get_all_transaction()
    data_manipulation.set_category_by_business(data, business_name, category)
    AppSettings.settings.db_instance.store_all_transaction(data)


def categorize_by_transaction_id(category: TransactionCategory, transaction_id: str):
    data = AppSettings.settings.db_instance.get_all_transaction()
    data_manipulation.set_category_by_transaction_id(data, transaction_id, category)
    AppSettings.settings.db_instance.store_all_transaction(data)
