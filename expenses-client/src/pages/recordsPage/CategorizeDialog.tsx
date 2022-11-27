import * as React from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import { Box } from "@mui/system";
import { TransactionCategory } from "../../common/models";
import { faCreditCard } from "@fortawesome/free-regular-svg-icons";
import {
  faBurger,
  faCarSide,
  faChampagneGlasses,
  faCircleCheck,
  faDroplet,
  faHouseChimney,
  faHouseUser,
  faKitchenSet,
  faMobileScreen,
  faMotorcycle,
  faSackDollar,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { alpha, Stack, styled, Typography } from "@mui/material";
import { COLOR_PALETTE } from "../../common/style/palette";

interface CategorizeDialogProps {
  children: React.ReactElement;
  category?: TransactionCategory;
  onClose?: () => void;
  onSave: (category?: TransactionCategory) => void;
}

export const CATEGORIES = [
  {
    name: TransactionCategory.HOME_UTILS,
    icon: faHouseUser,
    text: "Maintenance",
    income: false,
  },
  { name: TransactionCategory.FOOD, icon: faKitchenSet, text: "Food" },
  {
    name: TransactionCategory.RESTAURANT,
    icon: faBurger,
    text: "Restaurant",
  },
  {
    name: TransactionCategory.DELIVERY,
    icon: faMotorcycle,
    text: "Delivery",
  },
  { name: TransactionCategory.FUN, icon: faChampagneGlasses, text: "Fun" },
  {
    name: TransactionCategory.SALARY,
    icon: faSackDollar,
    text: "Salary",
    income: true,
  },
  {
    name: TransactionCategory.CARD,
    icon: faCreditCard,
    text: "Credit",
  },
  { name: TransactionCategory.RENT, icon: faHouseChimney, text: "Rent" },
  { name: TransactionCategory.CAR, icon: faCarSide, text: "Car" },
  { name: TransactionCategory.BILLS, icon: faDroplet, text: "Bills" },
  {
    name: TransactionCategory.GADGETS,
    icon: faMobileScreen,
    text: "Gadgets",
  },
];

const CategoryOptionContainer = styled(Stack)<{ selected: boolean }>(
  ({ theme, selected }) => ({
    width: "100px",
    height: "100px",
    border: "1px solid black",
    borderRadius: "8px",
    margin: theme.spacing(1),
    padding: theme.spacing(1),
    backgroundColor: selected
      ? COLOR_PALETTE.INFO_CARD
      : alpha(COLOR_PALETTE.INFO_CARD, 0.3),
    "&:hover": {
      backgroundColor: alpha(COLOR_PALETTE.INFO_CARD, 0.9),
      cursor: "pointer",
    },
  })
);

export default function CategorizeDialog(props: CategorizeDialogProps) {
  const [open, setOpen] = React.useState(false);
  const [selected, setSelected] = React.useState<TransactionCategory>(
    props.category
  );

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    props.onClose();
  };

  const handleCancel = () => handleClose();
  // const handleDone = () => {
  //   saveAndClose(selected);
  // };
  const saveAndClose = (selection?: TransactionCategory) => {
    props.onSave(selection);
    handleClose();
  };

  const handleSelected = (Category: TransactionCategory) => () => {
    setSelected(selected !== Category ? Category : undefined);
    saveAndClose(selected !== Category ? Category : undefined);
  };

  return (
    <div>
      <Box onClick={handleClickOpen}>{props.children}</Box>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Categorize</DialogTitle>
        <DialogContent>
          <DialogContentText marginBottom={1}>
            Select transactions cateogry
          </DialogContentText>
          <Box maxWidth="600px" flexWrap="wrap" display="flex">
            {CATEGORIES.map((category) => (
              <CategoryOptionContainer
                selected={selected === category.name}
                onClick={handleSelected(category.name)}
              >
                <Stack
                  height="10%"
                  direction="row"
                  justifyContent="space-between"
                >
                  {selected === category.name ? (
                    <FontAwesomeIcon
                      icon={faCircleCheck}
                      color="green"
                      size="xl"
                    />
                  ) : (
                    <Box visibility="hidden"> - </Box>
                  )}
                </Stack>
                <Box
                  height="50%"
                  justifyContent="center"
                  alignItems="center"
                  display="flex"
                  padding={1}
                >
                  <FontAwesomeIcon icon={category.icon} size="4x" />
                </Box>
                <Typography padding={1} textAlign="center">
                  {category.text}
                </Typography>
              </CategoryOptionContainer>
            ))}
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCancel}>Cancel</Button>
          {/* <Button onClick={handleDone}>Done</Button> */}
        </DialogActions>
      </Dialog>
    </div>
  );
}
