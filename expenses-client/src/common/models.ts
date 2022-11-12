export interface StatisticModel {
  value: number | string;
  additional_info?: string;
}

export interface StatsModel {
  expenses: StatisticModel;
  income: StatisticModel;
  current_balance: StatisticModel;
  avg_expense_per_month: StatisticModel;
  avg_income_per_month: StatisticModel;
  avg_saving_per_month: StatisticModel;
  top_spending_amount: StatisticModel;
  top_spending_business: StatisticModel;
}

export interface RecordsModel {
  records: RecordModel[];
  sort_options: string[];
  aggregate_options: string[];
  type_options: string[];
}

export enum TransactionCategory {
  HOME_UTILS = "home_utils",
  FOOD = "food",
  RESTAURANT = "restaurant",
  DELIVERY = "delivery",
  FUN = "fun",
  SALARY = "salary",
  CARD = "card",
  RENT = "rent",
  CAR = "car",
}

export enum TransactionType {
  CARD = "CARD",
  BANK = "BANK",
}

export interface RecordModel {
  t_id?: string;
  t_date?: string;
  money?: number;
  business?: string;
  card?: string;
  category?: TransactionCategory;
  t_type?: TransactionType;
  count?: string;
  avg?: string;
}

export interface RecordsSelection {
  aggregate?: string;
  sort_by?: string;
  include?: string;
  desc?: boolean;
}

export interface RecordsUpdate {
  category?: TransactionCategory;
}
