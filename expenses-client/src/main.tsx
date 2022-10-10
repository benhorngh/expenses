import { QueryClientProvider } from "react-query";
import { queryClient } from "./common/reactQueryClient";
import Routes from "./routes";

const Main: React.FC = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <Routes />
    </QueryClientProvider>
  );
};

export default Main;
