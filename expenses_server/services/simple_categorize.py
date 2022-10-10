import pandas as pd

from expenses_server.common.models import TransactionCategory


def categorize_transactions(df: pd.DataFrame):
    df['category'] = df['money'].map(lambda v: TransactionCategory.EXPENSE.value if v < 0 else TransactionCategory.INCOME.value)
