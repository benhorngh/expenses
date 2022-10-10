import { BrowserRouter, Route, Routes as DomRoutes } from "react-router-dom";
import AppWrapper from "./pageComponents/appWrapper";
import AboutPage from "./pages/aboutPage";
import HomePage from "./pages/homePage/homePage";
import MorePage from "./pages/morePage";

const Routes: React.FC = () => {
  return (
    <BrowserRouter>
      <DomRoutes>
        <Route path="/about" element={<AppWrapper element={AboutPage} />} />
        <Route path="/more" element={<AppWrapper element={MorePage} />} />
        <Route path="/*" element={<AppWrapper element={HomePage} />} />
      </DomRoutes>
    </BrowserRouter>
  );
};

export default Routes;
