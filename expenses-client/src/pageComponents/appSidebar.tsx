import { styled, Theme, CSSObject } from "@mui/material/styles";
import MuiDrawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faAddressCard,
  faFilter,
  faHome,
} from "@fortawesome/free-solid-svg-icons";
import NavigationItem from "./NavigationItem";
import { sidebarWidth } from "../common/constants";
import { useNavigate } from "react-router-dom";

const openedMixin = (theme: Theme): CSSObject => ({
  width: sidebarWidth,
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: "hidden",
});

const closedMixin = (theme: Theme): CSSObject => ({
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: "hidden",
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up("sm")]: {
    width: `calc(${theme.spacing(8)} + 1px)`,
  },
});

export const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  justifyContent: "flex-end",
  padding: theme.spacing(0, 1),
  ...theme.mixins.toolbar,
}));

const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  position: "absolute",
  width: sidebarWidth,
  flexShrink: 0,
  whiteSpace: "nowrap",
  boxSizing: "border-box",
  ...(open && {
    ...openedMixin(theme),
    "& .MuiDrawer-paper": openedMixin(theme),
  }),
  ...(!open && {
    ...closedMixin(theme),
    "& .MuiDrawer-paper": closedMixin(theme),
  }),
}));

export interface AppSidebarProps {
  open: boolean;
  setOpen: (open: boolean) => void;
}
export default function AppSidebar(props: AppSidebarProps) {
  const navigate = useNavigate();

  const navigateTo = (to: string) => () => {
    navigate(to);
  };
  return (
    <Drawer variant="permanent" open={props.open}>
      <DrawerHeader>
        <IconButton onClick={() => props.setOpen(false)}>
          <ChevronLeftIcon sx={{ display: props.open ? "block" : "none" }} />
        </IconButton>
      </DrawerHeader>
      <Divider />
      <List>
        <NavigationItem
          text="home"
          icon={<FontAwesomeIcon icon={faHome} />}
          open={props.open}
          onClick={navigateTo("/")}
        />
      </List>
      <Divider />
      <List>
        <NavigationItem
          text="records"
          icon={<FontAwesomeIcon icon={faFilter} />}
          open={props.open}
          onClick={navigateTo("/records")}
        />
        <NavigationItem
          text="about"
          icon={<FontAwesomeIcon icon={faAddressCard} />}
          open={props.open}
          onClick={navigateTo("/about")}
        />
      </List>
    </Drawer>
  );
}
