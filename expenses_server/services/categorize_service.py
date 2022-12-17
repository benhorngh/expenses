import traceback
from typing import List

import pandas as pd

from expenses_server.common.models import TransactionCategory, Rule, RuleType
from expenses_server.common.settings import AppSettings
from expenses_server.services import data_manipulation


def handle_data(func):
    def handler(*args, **kwargs):
        data = AppSettings.globals.transaction_db.get_all_data()
        results = func(*args, **kwargs, data=data)
        AppSettings.globals.transaction_db.store_all_data(data)
        return results

    return handler


@handle_data
def categorize_by_business_name(category: TransactionCategory, business_name: str, data: pd.DataFrame = None):
    data_manipulation.set_category_by_business(data, business_name, category)
    add_rule(Rule(r_type=RuleType.business_name, value=business_name, category=category))


@handle_data
def categorize_by_transaction_id(category: TransactionCategory, transaction_id: str, data: pd.DataFrame = None):
    data_manipulation.set_category_by_transaction_id(data, transaction_id, category)
    add_rule(Rule(r_type=RuleType.transaction_id, value=transaction_id, category=category))


def add_rule(rule: Rule):
    data = AppSettings.globals.rules_db.get_all_data()
    data = pd.concat([data, pd.DataFrame(data=[rule.dict()])], ignore_index=True)
    AppSettings.globals.rules_db.store_all_data(data)


def apply_rules(transactions: pd.DataFrame):
    rules_df = AppSettings.globals.rules_db.get_all_data()
    rules = convert_to_rules(rules_df)
    for rule in rules:
        if rule.r_type == RuleType.transaction_id:
            data_manipulation.set_category_by_transaction_id(transactions, rule.value, rule.category)
        if rule.r_type == RuleType.business_name:
            data_manipulation.set_category_by_business(transactions, rule.value, rule.category)


def convert_to_rules(data: pd.DataFrame) -> List[Rule]:
    rules = []
    for r in data.to_dict('records'):
        try:
            rules.append(Rule(**r))
        except:
            traceback.print_exc()
            raise
    return rules
