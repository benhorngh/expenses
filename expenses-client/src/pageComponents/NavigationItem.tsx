import {
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from "@mui/material";

interface NavigationItemProps {
  text: string;
  icon: React.ReactNode;
  open: boolean;
  onClick: () => void;
}

export default function NavigationItem(props: NavigationItemProps) {
  const { open, text, icon } = props;
  return (
    <ListItem
      key={text}
      disablePadding
      sx={{ display: "block" }}
      onClick={props.onClick}
    >
      <ListItemButton
        sx={{
          minHeight: 48,
          justifyContent: open ? "initial" : "center",
          px: 2.5,
        }}
      >
        <ListItemIcon
          sx={{
            minWidth: 0,
            mr: open ? 3 : "auto",
            justifyContent: "center",
          }}
        >
          {icon}
        </ListItemIcon>
        <ListItemText primary={text} sx={{ opacity: open ? 1 : 0 }} />
      </ListItemButton>
    </ListItem>
  );
}
