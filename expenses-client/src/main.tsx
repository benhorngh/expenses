import { ThemeProvider } from "@mui/material";
import { QueryClientProvider } from "react-query";
import { queryClient } from "./common/reactQueryClient";
import { appTheme } from "./common/style/muiTheme";
import Routes from "./routes";

const Main: React.FC = () => {
  return (
    <ThemeProvider theme={appTheme}>
      <QueryClientProvider client={queryClient}>
        <Routes />
      </QueryClientProvider>
    </ThemeProvider>
  );
};

export default Main;
