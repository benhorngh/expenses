import { Box, Divider } from "@mui/material";
import { useGetStates } from "../../common/api";
import { BasePageProps } from "../../pageComponents/appWrapper";
import { ErrorPage } from "../components/error";
import { PageLoader } from "../components/loader";
import { BigStatsSection, SmallStatsSection } from "./statsSections";

const HomePage: React.FC<BasePageProps> = (props) => {
  const getStats = useGetStates();

  if (getStats.isLoading) {
    return <PageLoader />;
  }

  if (getStats.isError) {
    return <ErrorPage />;
  }

  return (
    <Box paddingLeft={25} paddingRight={15}>
      <BigStatsSection stats={getStats.data} />
      <Divider sx={{ marginY: 5 }} />
      <SmallStatsSection stats={getStats.data} />
    </Box>
  );
};
export default HomePage;
