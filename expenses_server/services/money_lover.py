import traceback
from typing import List

from tqdm import tqdm

from expenses_server.common.models import Transaction, TransactionCategory
from expenses_server.services.money_lover_driver import MoneyLover

MY_CATEGORY_TO_MONEY_LOVER = {TransactionCategory.HOME_UTILS: 'Home Maintenance',
                              TransactionCategory.FOOD: 'food',
                              TransactionCategory.RESTAURANT: 'restaurants',
                              TransactionCategory.DELIVERY: 'delivery',
                              TransactionCategory.FUN: 'travel',
                              TransactionCategory.CAR: 'transportation',
                              TransactionCategory.SALARY: 'salary',
                              TransactionCategory.RENT: 'rentals',
                              TransactionCategory.CARD: 'credit card',
                              TransactionCategory.GADGETS: 'personal items',
                              TransactionCategory.BILLS: 'other utility bills',
                              TransactionCategory.UNKNOWN_INCOME: 'incoming',
                              TransactionCategory.UNKNOWN_EXPENSE: 'outgoing'
                              }


def send_to_money_lover(transactions: List[Transaction], wallet_name: str, authorization_token: str):
    MoneyLover.init_data(authorization_token)
    transactions_to_money_lover(wallet_name, transactions)


def transactions_to_money_lover(wallet_name, transactions: List[Transaction]):
    wallet_id = MoneyLover.get_wallet_id_by_name(wallet_name)
    failed = []
    for t, i in tqdm(zip(transactions, range(1, len(transactions))), total=len(transactions)):
        try:
            add_to_money_lover_wallet(wallet_id, t)
        except:
            traceback.print_exc()
            failed.append(t)
    print(f'failed: {len(failed)} out of {len(transactions)}')
    print(failed)


def get_category_id_by_category(category: TransactionCategory, wallet_id: str):
    money_lover_cat = MY_CATEGORY_TO_MONEY_LOVER.get(category)
    if not money_lover_cat:
        return None
    return MoneyLover.get_category_id_by_name(money_lover_cat.lower(), wallet_id)


def add_to_money_lover_wallet(wallet_id, transaction: Transaction):
    category_id = get_category_id_by_category(transaction.category, wallet_id)
    if not category_id:
        return
    # print(f"sending {wallet_id}, {transaction.t_date}, {abs(transaction.money)}, {transaction.business}, {category_id}")
    MoneyLover.add_to_wallet(account_id=wallet_id,
                             transaction_date=transaction.t_date,
                             amount=abs(transaction.money),
                             note=transaction.business,
                             category_id=category_id)
