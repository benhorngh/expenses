import { faEye, faEyeSlash } from "@fortawesome/free-regular-svg-icons";
import {
  faArrowDown19,
  faArrowLeft,
  faArrowRight,
  faArrowUp91,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Button, Divider, IconButton, Typography } from "@mui/material";
import { Stack } from "@mui/system";
import { useSearchParams } from "react-router-dom";
import { useGetRecords } from "../../common/api";
import { RecordModel } from "../../common/models";
import { PageLoader } from "../components/loader";
import BasicSelect from "./BasicSelect";
import TransactionRow from "./TransactionRow";

const RecordsPage: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();

  const aggregate = searchParams.get("aggregate");
  const include = searchParams.get("include");
  const sortBy = searchParams.get("sort") || "date";
  const desc = searchParams.get("desc") === "true";
  const page = parseInt(searchParams.get("page")) || 1;
  const hideCategorized = searchParams.get("hideCategorized") === "true";

  const getRecords = useGetRecords({
    aggregate: aggregate,
    sort_by: sortBy,
    include: include,
    desc: desc,
  });

  const updateSeachParam = (key: string, value?: string) => {
    if (value) searchParams.set(key, value);
    else searchParams.delete(key);
    setSearchParams(searchParams);
  };

  const handleAggregateChange = (newValue?: string) => {
    updateSeachParam("aggregate", newValue);
  };
  const handleSortByChange = (newValue?: string) => {
    updateSeachParam("sort", newValue);
  };
  const handleIncludeChange = (newValue?: string) => {
    updateSeachParam("include", newValue);
  };

  const handleSortDirectionClick = () => {
    updateSeachParam("desc", !desc ? "true" : "false");
  };

  const handleHideCategorizedClick = () => {
    updateSeachParam("hideCategorized", !hideCategorized ? "true" : "false");
  };

  const handlePageChange = (back: boolean) => () =>
    updateSeachParam("page", (back ? (page || 1) - 1 : (page || 1) + 1) + "");

  if (getRecords.isLoading) {
    return <PageLoader />;
  }
  return (
    <Stack spacing={3}>
      <Stack direction="row" justifyContent="space-between" width="100%">
        <Stack direction="row" spacing={3} alignItems="center">
          <BasicSelect
            selected={include}
            onChange={handleIncludeChange}
            options={getRecords.data.type_options || []}
            label="Include"
          />
          <BasicSelect
            selected={aggregate}
            onChange={handleAggregateChange}
            options={getRecords.data.aggregate_options || []}
            label="Aggregate by"
            allowEmpty
          />
          <Stack direction="row" justifyContent="center" alignItems="center">
            <BasicSelect
              selected={sortBy}
              onChange={handleSortByChange}
              options={getRecords.data.sort_options || []}
              label="Sort by"
              allowEmpty={false}
            />
            <IconButton
              color="primary"
              component="label"
              sx={{ width: 36, height: 36 }}
              onClick={handleSortDirectionClick}
            >
              <FontAwesomeIcon
                icon={desc ? faArrowDown19 : faArrowUp91}
                size="xs"
              />
            </IconButton>
            <Button
              color="secondary"
              component="label"
              onClick={handleHideCategorizedClick}
              variant="text"
              sx={{ margin: 2, textTransform: "none" }}
            >
              <FontAwesomeIcon icon={hideCategorized ? faEyeSlash : faEye} />

              <Typography padding={1} variant="body2">
                Categorized
              </Typography>
            </Button>
          </Stack>
        </Stack>
        <Stack justifyContent="center" padding={4} spacing={2} direction="row">
          <IconButton
            color="primary"
            component="label"
            sx={{ width: 36, height: 36 }}
            onClick={handlePageChange(true)}
            disabled={page === 1}
          >
            <FontAwesomeIcon icon={faArrowLeft} />
          </IconButton>

          <Typography variant="h5">{page}</Typography>
          <IconButton
            color="primary"
            component="label"
            sx={{ width: 36, height: 36 }}
            onClick={handlePageChange(false)}
          >
            <FontAwesomeIcon icon={faArrowRight} />
          </IconButton>
        </Stack>
      </Stack>
      <Divider flexItem orientation="horizontal" />
      <Stack direction="row" flexWrap="wrap">
        {getRecords.data.records
          .filter((t) => (hideCategorized ? !!!t.category : true))
          .slice((page - 1) * 100, page * 100)
          .map((record: RecordModel, index: number) => (
            <TransactionRow record={record} key={index} />
          ))}
      </Stack>
    </Stack>
  );
};

export default RecordsPage;
