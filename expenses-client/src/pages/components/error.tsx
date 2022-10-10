import { faWarning } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Stack, Typography } from "@mui/material";

export const ErrorPage: React.FC = () => {
  return (
    <Stack
      width="100%"
      height="100%"
      alignItems="center"
      justifyContent="center"
      spacing={3}
    >
      <FontAwesomeIcon fontSize={50} icon={faWarning} color="red" />
      <Typography variant="h3">Error occurred, try again later.</Typography>
    </Stack>
  );
};
