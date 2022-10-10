import traceback
from typing import List

from tqdm import tqdm

from expenses_server.common.models import Transaction, TransactionCategory
from expenses_server.services.money_lover_driver import MoneyLover

MY_CATEGORY_TO_MONEY_LOVER = {TransactionCategory.INCOME: "income", TransactionCategory.EXPENSE: "outgoing"}


def send_to_money_lover(transactions: List[Transaction], wallet_name, authorization_token: str):
    MoneyLover.init_data(authorization_token)
    transactions_to_money_lover(wallet_name, transactions)


def transactions_to_money_lover(wallet_name, transactions: List[Transaction]):
    wallet_id = MoneyLover.get_wallet_id_by_name(wallet_name)
    failed = []
    for t, i in tqdm(zip(transactions, range(1, len(transactions)))):
        try:
            add_to_money_lover_wallet(wallet_id, t)
        except:
            traceback.print_exc()
            failed.append(t)
    print(f'failed: {len(failed)} out of {len(transactions)}')


def get_category_id_by_category(category: TransactionCategory, wallet_id: str):
    money_lover_cat = MY_CATEGORY_TO_MONEY_LOVER.get(category)
    if not money_lover_cat:
        return None
    return MoneyLover.get_category_id_by_name(money_lover_cat.lower(), wallet_id)


def add_to_money_lover_wallet(wallet_id, transaction: Transaction):
    category_id = get_category_id_by_category(transaction.category, wallet_id)
    if not category_id:
        return
    MoneyLover.add_to_wallet(account_id=wallet_id,
                             transaction_date=transaction.t_date,
                             amount=abs(transaction.money),
                             note=transaction.business,
                             category_id=category_id)
