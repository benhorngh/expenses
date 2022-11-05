import { createTheme } from "@mui/material";
import { COLOR_PALETTE } from "./palette";

export const appTheme = createTheme({
  palette: {
    primary: {
      main: COLOR_PALETTE.PRIMARY,
    },
    secondary: {
      main: COLOR_PALETTE.SECONDERY,
    },
  },
});
