import {
  faCircleInfo,
  faEllipsisVertical,
  faShoppingBag,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  IconButton,
  ListItemIcon,
  ListItemText,
  Menu,
  MenuItem,
} from "@mui/material";
import { useState } from "react";
import { useUpdateRecords } from "../../common/api";
import { RecordModel, TransactionCategory } from "../../common/models";
import CategorizeDialog from "./CategorizeDialog";

interface RecordOptionsProps {
  record: RecordModel;
}

const RecordOptions: React.FC<RecordOptionsProps> = (props) => {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };
  const changeRecordsCategory = useUpdateRecords();
  const onCategoryChange = async (category?: TransactionCategory) => {
    const data = {
      business: props.record.business,
      update: { category: category },
    };
    changeRecordsCategory.mutate(data);
  };
  return (
    <>
      <IconButton
        aria-controls={open ? "basic-menu" : undefined}
        aria-haspopup="true"
        aria-expanded={open ? "true" : undefined}
        onClick={handleClick}
        sx={{ height: 24, width: 24 }}
      >
        <FontAwesomeIcon icon={faEllipsisVertical} color="grey" size="xs" />
      </IconButton>
      <Menu
        id="basic-menu"
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        MenuListProps={{
          "aria-labelledby": "basic-button",
        }}
      >
        <CategorizeDialog onClose={handleClose} onSave={onCategoryChange}>
          <MenuItem>
            <ListItemIcon>
              <FontAwesomeIcon icon={faShoppingBag} color="grey" />
            </ListItemIcon>
            <ListItemText>Categorize</ListItemText>
          </MenuItem>
        </CategorizeDialog>

        <MenuItem onClick={handleClose}>
          <ListItemIcon>
            <FontAwesomeIcon icon={faCircleInfo} color="grey" />
          </ListItemIcon>
          <ListItemText>Info</ListItemText>
        </MenuItem>
      </Menu>
    </>
  );
};

export default RecordOptions;
