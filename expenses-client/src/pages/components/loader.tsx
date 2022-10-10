import {
  Box,
  CircularProgress,
  circularProgressClasses,
  CircularProgressProps,
} from "@mui/material";

export function Loader(props: CircularProgressProps) {
  return (
    <Box sx={{ position: "relative" }}>
      <CircularProgress
        variant="determinate"
        sx={{
          color: (theme) =>
            theme.palette.grey[theme.palette.mode === "light" ? 200 : 800],
        }}
        size={40}
        thickness={4}
        {...props}
        value={100}
      />
      <CircularProgress
        variant="indeterminate"
        disableShrink
        sx={{
          color: (theme) =>
            theme.palette.mode === "light" ? "#1a90ff" : "#308fe8",
          animationDuration: "550ms",
          position: "absolute",
          left: 0,
          [`& .${circularProgressClasses.circle}`]: {
            strokeLinecap: "round",
          },
        }}
        size={40}
        thickness={4}
        {...props}
      />
    </Box>
  );
}

export const PageLoader: React.FC = () => {
  return (
    <Box
      width="100%"
      height="100%"
      alignContent="center"
      justifyContent="center"
    >
      <Box position="absolute" left="50%" top="40%">
        <Loader />
      </Box>
    </Box>
  );
};
