import { BrowserRouter, Route, Routes as DomRoutes } from "react-router-dom";
import AppWrapper from "./pageComponents/appWrapper";
import AboutPage from "./pages/aboutPage";
import HomePage from "./pages/homePage/homePage";
import MorePage from "./pages/recordsPage/RecordsPage";

const Routes: React.FC = () => {
  return (
    <BrowserRouter>
      <DomRoutes>
        <Route
          path="/about"
          element={<AppWrapper children={<AboutPage />} />}
        />
        <Route
          path="/records"
          element={<AppWrapper children={<MorePage />} />}
        />
        <Route path="/*" element={<AppWrapper children={<HomePage />} />} />
      </DomRoutes>
    </BrowserRouter>
  );
};

export default Routes;
