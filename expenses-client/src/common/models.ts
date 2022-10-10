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
