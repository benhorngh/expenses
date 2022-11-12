import { alpha, Box, Grid, styled } from "@mui/material";
import { renderDate } from "../../common/dateUtils";
import { RecordModel } from "../../common/models";
import { COLOR_PALETTE } from "../../common/style/palette";
import { renderMoney } from "../../common/utils";
import RecordOptions from "./RecordOptions";

interface TransactionRowProps {
  record: RecordModel;
}

const RecordContainer = styled(Box)<{ cardcolor: string }>(
  ({ theme, cardcolor }) => ({
    border: `1px solid ${cardcolor}`,
    borderRadius: "8px",
    padding: theme.spacing(2),
    backgroundColor: alpha(cardcolor, 0.3),
    "&:hover": {
      backgroundColor: alpha(cardcolor, 0.9),
      cursor: "pointer",
    },
  })
);

const TransactionRow: React.FC<TransactionRowProps> = (props) => {
  const cardColor =
    props.record.money < 0 ? COLOR_PALETTE.EXPENSE : COLOR_PALETTE.INCOME;

  return (
    <RecordContainer cardcolor={cardColor}>
      <Grid container>
        <Grid item xs={2}>
          {renderMoney(props.record.money)}
        </Grid>
        <Grid item xs={4}>
          {props.record.business}
        </Grid>
        {props.record.t_date && (
          <Grid item xs={2}>
            {renderDate(props.record.t_date) || ""}
          </Grid>
        )}
        <Grid item xs>
          {props.record.category}
        </Grid>
        <Grid item xs={1}>
          <RecordOptions record={props.record} />
        </Grid>
      </Grid>
    </RecordContainer>
  );
};

export default TransactionRow;
