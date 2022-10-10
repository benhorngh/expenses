from expenses_server.common.models import StatisticsResponseModel

from expenses_server.services import data_manipulation
from expenses_server.common.settings import AppSettings


def get_statistics() -> StatisticsResponseModel:
    data = AppSettings.settings.db_instance.get_all_transaction()
    data_manipulation.prepare_date(data)
    statistics_results = StatisticsResponseModel(expenses=data_manipulation.get_bank_total_expense(data),
                                                 income=data_manipulation.get_bank_total_income(data),
                                                 current_balance=data_manipulation.get_bank_total_balance(data),
                                                 avg_expense_per_month=data_manipulation.get_avg_expense_per_month(data),
                                                 avg_income_per_month=data_manipulation.get_avg_income_per_month(data),
                                                 avg_saving_per_month=data_manipulation.get_avg_saving_per_month(data),
                                                 top_spending_amount=data_manipulation.get_top_spending_amount(data),
                                                 top_spending_business=data_manipulation.get_top_spending_business(data)
                                                 )
    return statistics_results
