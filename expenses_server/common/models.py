from datetime import datetime
from enum import Enum
from typing import Union, Optional, List

import pydantic
from pydantic import BaseModel


class TransactionCategory(str, Enum):
    HOME_UTILS = 'home_utils'
    FOOD = 'food'
    RESTAURANT = 'restaurant'
    DELIVERY = 'delivery'
    FUN = 'fun'
    CAR = 'car'
    SALARY = 'salary'
    RENT = 'rent'
    CARD = 'card'
    GADGETS = 'gadgets'
    BILLS = 'bills'
    UNKNOWN_INCOME = 'unknown_income'
    UNKNOWN_EXPENSE = 'unknown_expense'
    IGNORE = 'ignore'
    SHOPPING = 'shopping'
    TRANSPORTATION = 'transportation'


class TransactionType(str, Enum):
    BANK = 'bank'
    CARD = 'card'


class SpecialTypeId(str, Enum):
    BANK_LEUMI = 'leumi'
    BANK_PEPPER = 'pepper'
    CREDIT_CARD_CAL = 'cal'


class Transaction(BaseModel):
    t_id: str = None
    t_date: datetime = None
    money: float = None
    business: str = None
    category: TransactionCategory = None
    t_type: TransactionType = None
    type_id: str = None


class Record(Transaction):
    t_id: str = None
    t_date: datetime = None
    money: float = None
    business: str = None
    category: TransactionCategory = None
    t_type: TransactionType = None
    type_id: str = None
    count: str = 1
    avg: str = None


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


class RecordsResponseModel(BaseModel):
    records: List[Record]
    type_options: List[str]
    sort_options: List[str]
    aggregate_options: List[str]


class RecordsUpdate(BaseModel):
    category: Optional[TransactionCategory] = None


class ChangeCategoryRequest(BaseModel):
    businesses: Optional[List[str]] = None
    transactions_ids: Optional[List[str]] = None
    record: RecordsUpdate


class AggregateBy(Enum):
    BUSINESS = 'business'
    MONTH = 'month'
    TYPE = 'type'


class SortBy(Enum):
    DATE = 'date'
    AMOUNT = 'amount'


class Include(Enum):
    ALL = 'all'
    CARD = 'card'
    BANK = 'bank'


class RecordsRequest(BaseModel):
    aggregate: Optional[AggregateBy]
    sort_by: Optional[SortBy]
    include: Optional[Include]
    desc: Optional[bool]


class C(str, Enum):
    T_ID = 't_id'
    T_DATE = "t_date"
    BUSINESS = "business"
    MONEY = "money"
    CATEGORY = "category"
    T_TYPE = "t_type"
    TYPE_ID = "type_id"


class N(str, Enum):
    IS_INCOME = 'is_income'
    MONTH = 'n_date'
    COUNT = 'count'
    AVG = 'avg'


class RuleType(str, Enum):
    transaction_id = 'TRANSACTION_ID'
    business_name = 'BUSINESS_NAME'


class Rule(BaseModel):
    r_type: RuleType
    value: str
    category: TransactionCategory

