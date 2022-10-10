from datetime import datetime
from enum import Enum
from typing import Union, Optional

import pydantic
from pydantic import BaseModel, validator


class TransactionCategory(Enum):
    INCOME = 'income'
    EXPENSE = 'expense'


class TransactionType(Enum):
    BANK = 'bank'
    CARD = 'card'


class Transaction(BaseModel):
    t_id: str = None
    t_date: datetime = None
    money: float = None
    business: str = None
    card: str = None
    category: TransactionCategory = None
    t_type: TransactionType = None

    @validator('category', pre=True)
    def category_init(cls, v):
        if v and not isinstance(v, TransactionCategory):
            v = v.value
        return v

    @validator('t_type', pre=True)
    def type_init(cls, v):
        if v and not isinstance(v, TransactionType):
            v = v.value
        return v


class StatisticModel(BaseModel):
    value: Union[int, str]
    additional_info: Optional[str] = None


class StatisticsResponseModel(BaseModel):
    expenses: StatisticModel
    income: StatisticModel
    current_balance: StatisticModel
    avg_expense_per_month: StatisticModel
    avg_income_per_month: StatisticModel
    avg_saving_per_month: StatisticModel
    top_spending_amount: StatisticModel
    top_spending_business: StatisticModel

    @pydantic.validator("*", pre=True)
    def except_value_only(cls, value):
        if isinstance(value, (int, str)):
            return StatisticModel(value=value)
        return value


class C(str, Enum):
    T_DATE = "t_date"
    BUSINESS = "business"
    CARD = "card"
    MONEY = "money"
    CATEGORY = "category"
    T_TYPE = "t_type"


class N(str, Enum):
    MONTH = 'n_date'
