import { faCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Card, Typography } from "@mui/material";
import { Stack } from "@mui/system";
import { renderDate } from "../../common/dateUtils";
import { RecordModel } from "../../common/models";
import { COLOR_PALETTE } from "../../common/style/palette";
import { renderMoney } from "../../common/utils";
import Categorize from "./Categorize";

interface TransactionRowProps {
  record: RecordModel;
}

const TransactionRow: React.FC<TransactionRowProps> = (props) => {
  const color =
    props.record.money < 0 ? COLOR_PALETTE.EXPENSE : COLOR_PALETTE.INCOME;

  return (
    <Card
      sx={{
        width: "25%",
        backgroundColor: "grey",
        padding: 2,
        margin: 2,
      }}
    >
      <Stack direction="column">
        <Stack
          spacing={1}
          justifyContent="end"
          alignItems="center"
          width="100%"
          direction="row"
        >
          <Typography>
            {props.record.t_date ? renderDate(props.record.t_date) : ""}
          </Typography>
          <FontAwesomeIcon icon={faCircle} size="xs" color={color} />
        </Stack>
        <Stack alignItems="center" width="100%">
          <Typography variant="h6">{props.record.business}</Typography>
          <Typography variant="h5">
            {renderMoney(props.record.money)}
          </Typography>
        </Stack>
      </Stack>
      <Categorize
        currentCategory={props.record.category}
        businesses={props.record.business ? [props.record.business] : []}
        transactionsIds={props.record.t_id ? [props.record.t_id] : []}
      />
    </Card>
  );
};

export default TransactionRow;
