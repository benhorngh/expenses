import {
  faSackDollar,
  faCreditCard,
  faWallet,
} from "@fortawesome/free-solid-svg-icons";
import { Stack } from "@mui/material";
import { StatsModel } from "../../common/models";
import { COLOR_PALETTE } from "../../common/style/palette";
import { BigStatistic, SmallStatistic } from "./stats";

interface StatsSectionProps {
  stats: StatsModel;
}

export const BigStatsSection: React.FC<StatsSectionProps> = (props) => {
  const stats = [
    {
      title: "Income",
      stat: props.stats.income,
      icon: faSackDollar,
      color: COLOR_PALETTE.INCOME,
    },
    {
      title: "Expense",
      stat: props.stats.expenses,
      icon: faCreditCard,
      color: COLOR_PALETTE.EXPENSE,
    },
    {
      title: "Current Balance",
      stat: props.stats.current_balance,
      icon: faWallet,
      color: "#E6E6FA",
    },
  ];

  return (
    <Stack
      direction="row"
      flexWrap="wrap"
      alignContent="flex-start"
      alignItems="flex-start"
    >
      {stats.map((stat, index) => (
        <BigStatistic key={index} {...stat} />
      ))}
    </Stack>
  );
};

export const SmallStatsSection: React.FC<StatsSectionProps> = (props) => {
  const stats = [
    {
      title: "Avarage expense for month",
      stat: props.stats.avg_expense_per_month,
    },
    {
      title: "Avarage income for month",
      stat: props.stats.avg_income_per_month,
    },
    {
      title: "Avarage saving for month",
      stat: props.stats.avg_saving_per_month,
    },
    {
      title: "#1 spending",
      stat: props.stats.top_spending_amount,
    },
    {
      title: "#1 business",
      stat: props.stats.top_spending_business,
      withoutCurrency: true,
    },
  ];

  return (
    <Stack
      direction="row"
      flexWrap="wrap"
      alignContent="flex-start"
      alignItems="flex-start"
    >
      {stats.map((statProps, index) => (
        <SmallStatistic
          key={index}
          color={COLOR_PALETTE.INFO_CARD}
          {...statProps}
        />
      ))}
    </Stack>
  );
};
