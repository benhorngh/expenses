import Box from "@mui/material/Box";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import { useState } from "react";
import { Typography } from "@mui/material";

interface BasicSelectProps {
  options: string[];
  onChange: (option?: string) => void;
  selected?: string;
  label: string;
  allowEmpty?: boolean;
}
export default function BasicSelect(props: BasicSelectProps) {
  const [selected, setSelected] = useState(props.selected || "");

  const handleChange = (event: SelectChangeEvent) => {
    const newValue = event.target.value as string;
    setSelected(newValue);
    props.onChange(newValue === "" ? undefined : newValue);
  };

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl sx={{ m: 1, minWidth: 120 }}>
        <Typography variant="caption" marginBottom={1}>
          {props.label}
        </Typography>

        <Select
          notched
          value={selected}
          onChange={handleChange}
          MenuProps={{ disableScrollLock: true }}
        >
          {props.allowEmpty && (
            <MenuItem value="">
              <em>None</em>
            </MenuItem>
          )}
          {props.options.map((option, index) => (
            <MenuItem value={option} key={index}>
              {option}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
}
