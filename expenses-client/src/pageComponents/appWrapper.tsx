import Box from "@mui/material/Box";
import { ReactElement, useState } from "react";
import AppHeader from "./appHeader";
import AppSidebar, { DrawerHeader } from "./appSidebar";

interface AppWrapperProps {
  children: ReactElement;
}

export default function AppWrapper(props: AppWrapperProps) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <Box>
      <AppHeader sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />
      <AppSidebar open={sidebarOpen} setOpen={setSidebarOpen} />
      <Box sx={{ flexGrow: 1, p: 3 }}>
        <DrawerHeader />
        <Box paddingLeft={25} paddingRight={15}>
          {props.children}
        </Box>
      </Box>
    </Box>
  );
}
