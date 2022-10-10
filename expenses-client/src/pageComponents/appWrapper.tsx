import Box from "@mui/material/Box";
import { useState } from "react";
import AppHeader from "./appHeader";
import AppSidebar, { DrawerHeader } from "./appSidebar";

export interface BasePageProps {
  sidebarOpen: boolean;
}

interface AppWrapperProps {
  element: React.FC<unknown & BasePageProps>;
}

export default function AppWrapper(props: AppWrapperProps) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <Box>
      <AppHeader sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />
      <AppSidebar open={sidebarOpen} setOpen={setSidebarOpen} />
      <Box sx={{ flexGrow: 1, p: 3 }}>
        <DrawerHeader />
        {props.element({ sidebarOpen })}
      </Box>
    </Box>
  );
}
