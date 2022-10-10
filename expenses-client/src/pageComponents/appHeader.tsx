import { styled } from "@mui/material/styles";
import MuiAppBar, { AppBarProps as MuiAppBarProps } from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import { sidebarWidth } from "../common/constants";

interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})<AppBarProps>(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(["width", "margin"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: sidebarWidth,
    width: `calc(100% - ${sidebarWidth}px)`,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

interface AppHeaderProps {
  sidebarOpen: boolean;
  setSidebarOpen: (open: boolean) => void;
}

export default function AppHeader(props: AppHeaderProps) {
  return (
    <AppBar
      position="fixed"
      open={props.sidebarOpen}
      sx={{ background: "transparent", boxShadow: "none" }}
    >
      <Toolbar>
        <IconButton
          color="inherit"
          aria-label="open drawer"
          onClick={() => props.setSidebarOpen(true)}
          edge="start"
          sx={{
            marginRight: 5,
            ...(props.sidebarOpen && { display: "none" }),
          }}
        >
          <FontAwesomeIcon icon={faBars} color="grey" />
        </IconButton>
      </Toolbar>
    </AppBar>
  );
}
