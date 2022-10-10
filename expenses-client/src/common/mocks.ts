import { StatsModel } from "./models";
export const statsModelMock: StatsModel = {
  expenses: { value: 1000 },
  income: { value: 3434 },
  current_balance: { value: 34343 },
  avg_expense_per_month: { value: 666 },
  avg_income_per_month: { value: 6768 },
  avg_saving_per_month: { value: 3434.4 },
  top_spending_amount: { value: 4545, additional_info: "At Ikea, 30.10.2020" },
  top_spending_business: { value: "Wolt", additional_info: "30 times" },
};
