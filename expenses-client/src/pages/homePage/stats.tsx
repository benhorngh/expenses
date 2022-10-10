import { IconDefinition } from "@fortawesome/fontawesome-svg-core";
import { faCircleQuestion } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Paper, alpha, Stack, Typography, Box, Tooltip } from "@mui/material";
import { CURRENCY_SIGN } from "../../common/constants";
import { StatisticModel } from "../../common/models";

interface BigStatisticProps {
  title: string;
  stat: StatisticModel;
  icon: IconDefinition;
  color: string;
  withoutCurrency?: boolean;
}

export const BigStatistic: React.FC<BigStatisticProps> = (props) => {
  return (
    <Paper
      sx={{
        backgroundColor: alpha(props.color, 0.3),
        margin: 2,
        padding: 5,
      }}
    >
      <Box width={200} height={100}>
        <Stack justifyContent="center" direction="column" spacing={2}>
          <Stack direction="row" spacing={1} alignItems="center">
            <FontAwesomeIcon icon={props.icon} color="#696969" />
            <Typography variant="body1" color="#696969">
              {props.title}
            </Typography>
          </Stack>
          <Stack direction="row" spacing={1} alignItems="end">
            {!props.withoutCurrency && (
              <Typography variant="body1" paddingBottom={1}>
                {CURRENCY_SIGN}
              </Typography>
            )}
            <Typography variant="h3">{props.stat.value}</Typography>
          </Stack>
        </Stack>
      </Box>
    </Paper>
  );
};

interface SmallStatisticProps {
  title: string;
  stat: StatisticModel;
  icon?: IconDefinition;
  color: string;
  withoutCurrency?: boolean;
}

export const SmallStatistic: React.FC<SmallStatisticProps> = (props) => {
  return (
    <Paper
      sx={{
        backgroundColor: alpha(props.color, 0.3),
        margin: 2,
        padding: 2,
      }}
    >
      <Box width={150} height={125} position="relative">
        {props.stat.additional_info && (
          <Box
            sx={{
              top: "0px",
              left: "0px%",
              position: "absolute",
              opacity: 0.5,
            }}
          >
            <Tooltip title={props.stat.additional_info} arrow>
              <FontAwesomeIcon icon={faCircleQuestion} color="#696969" />
            </Tooltip>
          </Box>
        )}
        <Box
          sx={{
            top: "0px",
            left: "50%",
            transform: "translateX(-50%)",
            position: "absolute",
          }}
        >
          {props.icon && <FontAwesomeIcon icon={props.icon} color="#696969" />}
        </Box>
        <Box position="absolute" top="25%" width="100%">
          <Stack
            direction="row"
            alignItems="end"
            spacing={1}
            width="100%"
            justifyContent="center"
          >
            {!props.withoutCurrency && (
              <Typography variant="body2" paddingBottom={1}>
                {CURRENCY_SIGN}
              </Typography>
            )}
            <Typography variant="h4">{props.stat.value}</Typography>
          </Stack>
        </Box>
        <Box position="absolute" bottom="0px" textAlign="center" width="100%">
          <Typography variant="body2" color="#696969">
            {props.title}
          </Typography>
        </Box>
      </Box>
    </Paper>
  );
};
