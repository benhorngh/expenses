import { faArrowDown19, faArrowUp91 } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Divider, IconButton } from "@mui/material";
import { Stack } from "@mui/system";
import { useState } from "react";
import { useGetRecords } from "../../common/api";
import { RecordModel } from "../../common/models";
import { PageLoader } from "../components/loader";
import BasicSelect from "./BasicSelect";
import TransactionRow from "./TransactionRow";

const RecordsPage: React.FC = () => {
  const [aggregate, setAggregate] = useState<string>();
  const [sortBy, setSortBy] = useState<string>("date");
  const [include, setInclude] = useState<string>();
  const [desc, setDesc] = useState(false);

  const getRecords = useGetRecords({
    aggregate: aggregate,
    sort_by: sortBy,
    include: include,
    desc: desc,
  });

  const handleAggregateChange = (newValue?: string) => {
    setAggregate(newValue);
  };
  const handleSortByChange = (newValue?: string) => {
    setSortBy(newValue);
  };
  const handleIncludeChange = (newValue?: string) => {
    setInclude(newValue);
  };

  const handleSortDirectionClick = () => setDesc(!desc);

  if (getRecords.isLoading) {
    // TODO handle search
    return <PageLoader />;
  }
  return (
    <Stack spacing={3}>
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
        </Stack>
      </Stack>
      <Divider flexItem orientation="horizontal" />
      <Stack direction="row" flexWrap="wrap">
        {getRecords.data.records
          .slice(0, 100)
          .map((record: RecordModel, index: number) => (
            <TransactionRow record={record} key={index} />
          ))}
      </Stack>
    </Stack>
  );
};

export default RecordsPage;
