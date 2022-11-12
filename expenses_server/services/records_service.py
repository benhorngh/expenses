from typing import List

import pandas as pd

from expenses_server.common.models import Transaction, RecordsResponseModel, RecordsRequest, AggregateBy, Record, \
    SortBy, Include
from expenses_server.common.settings import AppSettings
from expenses_server.services import data_manipulation


def get_records(search: RecordsRequest) -> RecordsResponseModel:
    data = AppSettings.settings.db_instance.get_all_transaction()
    data_manipulation.prepare_date(data)
    records = apply_search(data, search)
    return RecordsResponseModel(records=convert_to_transactions(records),
                                type_options=get_type_options(data),
                                sort_options=get_sort_options(data),
                                aggregate_options=get_aggregate_options(data)
                                )


def get_type_options(data: pd.DataFrame):
    return ['all', 'bank', 'card']


def get_sort_options(data: pd.DataFrame):
    return ['date', 'amount']


def get_aggregate_options(data: pd.DataFrame):
    return ['business', 'month']


def apply_search(data: pd.DataFrame, search: RecordsRequest):
    # filter
    if search.include and search.include == Include.CARD:
        data = data_manipulation.get_card_transactions(data)
    elif search.include and search.include == Include.BANK:
        data = data_manipulation.get_bank_transactions(data)

    # aggregate
    if search.aggregate and search.aggregate == AggregateBy.BUSINESS:
        data = data_manipulation.get_expense_by_business(data)
    elif search.aggregate and search.aggregate == AggregateBy.MONTH:
        data = data_manipulation.get_expense_by_month(data)

    # sort
    if search.sort_by and search.sort_by == SortBy.DATE:
        data = data_manipulation.sort_by_date(data, search.desc)
    elif search.sort_by and search.sort_by == SortBy.AMOUNT:
        data = data_manipulation.sort_by_amount(data, search.desc)
    return data


def convert_to_transactions(data: pd.DataFrame) -> List[Transaction]:
    transactions = [Transaction(**t) for t in data.to_dict('records')]
    return transactions


def convert_to_records(data: pd.DataFrame) -> List[Record]:
    records = [Record(**t) for t in data.to_dict('records')]
    return records
