import { faPlus } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Button, Stack, Typography } from "@mui/material";
import { useUpdateRecords } from "../../common/api";
import { TransactionCategory } from "../../common/models";
import CategorizeDialog, { CATEGORIES } from "./CategorizeDialog";

interface CategorizeProps {
  businesses?: string[];
  transactionsIds?: string[];
  currentCategory?: TransactionCategory;
}

const getCategoryInfo = (category: TransactionCategory) => {
  return CATEGORIES.find((c) => c.name === category);
};

const Categorize: React.FC<CategorizeProps> = (props) => {
  const changeRecordsCategory = useUpdateRecords();
  const onCategoryChange = async (category?: TransactionCategory) => {
    const data = {
      businesses: props.businesses,
      transactions_ids: props.transactionsIds,
      update: { category: category },
    };
    changeRecordsCategory.mutate(data);
  };
  const categoryInfo = getCategoryInfo(props.currentCategory);
  return (
    <>
      <CategorizeDialog
        onSave={onCategoryChange}
        category={props.currentCategory}
      >
        <Button variant={categoryInfo ? "text" : "outlined"}>
          <Stack
            direction="row"
            spacing={1}
            justifyContent="center"
            alignItems="center"
          >
            <FontAwesomeIcon
              icon={categoryInfo ? categoryInfo.icon : faPlus}
              color="grey"
            />
            <Typography>{categoryInfo ? categoryInfo.text : "Add"}</Typography>
          </Stack>
        </Button>
      </CategorizeDialog>
    </>
  );
};

export default Categorize;
