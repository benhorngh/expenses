import pandas as pd

from expenses_server.common.models import TransactionType, C, N, StatisticModel
from expenses_server.services import simple_categorize, user_interface_service


def numpy_to_int(func):
    def wrapper(*args, **kwargs):
        return int(func(*args, **kwargs))
    return wrapper


def prepare_date(df: pd.DataFrame):
    add_month_column(df)


def add_month_column(df: pd.DataFrame):
    df[N.MONTH.value] = df[C.T_DATE].map(lambda d: d.replace(day=1))


def get_bank_transactions(df: pd.DataFrame) -> pd.DataFrame:
    return df[df[C.T_TYPE] == TransactionType.BANK]


def get_card_transactions(df: pd.DataFrame) -> pd.DataFrame:
    return df[df[C.T_TYPE] == TransactionType.CARD]


def categorize_income_outcome(df: pd.DataFrame):
    simple_categorize.categorize_transactions(df)
    return df


def get_average_per_category(df: pd.DataFrame):
    return df.groupby("category")['money'].mean()


def get_average_per_category_per_month(df: pd.DataFrame):
    categories = df['category'].unique()
    df['month'] = df['t_date'].map(lambda d: f'{d.year}-{d.month}')
    categories_df = pd.DataFrame()
    for category in categories:
        category_df = df[df['category'] == category]
        category_df = category_df.groupby("month")['money'].sum()
        category_df = category_df.reset_index()
        category_df['category'] = category
        categories_df = pd.concat([categories_df, category_df], ignore_index=True)
    return categories_df


def get_expense_by_business(df: pd.DataFrame):
    # name, count, sum, avg
    df = df[df['t_type'] == TransactionType.CARD]
    data = []
    for business in df['business'].unique():
        bus_df = df[df['business'] == business]
        data.append(
            {"name": business, "count": len(bus_df), "sum": bus_df['money'].sum(), "avg": bus_df['money'].mean()})
    return pd.DataFrame(data=data).sort_values(by=['count'], ascending=False, ignore_index=True)


def get_expenses(df: pd.DataFrame) -> pd.DataFrame:
    return df[df[C.MONEY] < 0]


def get_income(df: pd.DataFrame) -> pd.DataFrame:
    return df[df[C.MONEY] > 0]


@numpy_to_int
def get_bank_total_expense(df: pd.DataFrame) -> int:
    # return df[(df[C.T_TYPE] == TransactionType.BANK) & (df[C.MONEY] < 0)][C.MONEY].sum()
    data = get_bank_transactions(df)
    data = get_expenses(data)
    return data[C.MONEY].sum()


@numpy_to_int
def get_bank_total_income(df: pd.DataFrame) -> int:
    # return df[(df[C.T_TYPE] == TransactionType.BANK) & (df[C.MONEY] > 0)][C.MONEY].sum()
    data = get_bank_transactions(df)
    data = get_income(data)
    return data[C.MONEY].sum()


@numpy_to_int
def get_bank_total_balance(df: pd.DataFrame) -> int:
    data = get_bank_transactions(df)
    return data[C.MONEY].sum()


@numpy_to_int
def get_avg_per_month(df: pd.DataFrame) -> int:
    month_to_expense = df[[N.MONTH, C.MONEY]].groupby(N.MONTH).sum()
    return month_to_expense.mean()


@numpy_to_int
def get_avg_expense_per_month(df: pd.DataFrame) -> int:
    return get_avg_per_month(get_expenses(get_bank_transactions(df)))


@numpy_to_int
def get_avg_income_per_month(df: pd.DataFrame) -> int:
    return get_avg_per_month(get_income(get_bank_transactions(df)))


def get_avg_saving_per_month(df: pd.DataFrame) -> int:
    return get_avg_income_per_month(df) + get_avg_expense_per_month(df)


def get_top_spending_amount(df: pd.DataFrame) -> StatisticModel:
    card_expenses = get_expenses(get_card_transactions(df))
    top_transaction = card_expenses[card_expenses[C.MONEY] == card_expenses[C.MONEY].min()].head(1)
    return StatisticModel(value=top_transaction[C.MONEY],
                          additional_info=user_interface_service.single_transaction(
                              top_transaction[C.BUSINESS].values[0],
                              pd.to_datetime(top_transaction[C.T_DATE].values[0])))


def get_top_spending_business(df: pd.DataFrame) -> StatisticModel:
    card_expenses = get_expenses(get_card_transactions(df))
    businesses = card_expenses[[C.BUSINESS, C.T_DATE, C.MONEY]].groupby(C.BUSINESS).agg({C.T_DATE: 'count',
                                                                                         C.MONEY: 'sum'}).reset_index()
    top_business = businesses[businesses[C.MONEY] == businesses[C.MONEY].min()].head(1)
    return StatisticModel(value=top_business[C.MONEY].values[0],
                          additional_info=user_interface_service.business_visits(top_business[C.BUSINESS].values[0],
                                                                                 top_business[C.T_DATE].values[0]))
