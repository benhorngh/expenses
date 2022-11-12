import {
  RecordsModel,
  RecordsSelection,
  RecordsUpdate,
  StatsModel,
} from "./models";
import { useMutation, useQuery } from "react-query";
import httpClient from "./httpClient";

async function getStats() {
  const { data } = await httpClient.get<StatsModel>("/statistics");
  return data;
}

export function useGetStates() {
  return useQuery(["stats"], getStats);
}

async function getRecords(recordsSelect: RecordsSelection) {
  const { data } = await httpClient.get<RecordsModel>("/records", {
    params: recordsSelect,
  });
  return data;
}

export function useGetRecords(recordsSelect: RecordsSelection) {
  return useQuery(["records", recordsSelect], () => getRecords(recordsSelect));
}

async function updateRecords(business, update: RecordsUpdate) {
  const { data } = await httpClient.patch<RecordsModel>(
    "/records",
    { update: update },
    {
      params: { business_name: business },
    }
  );
  return data;
}

export function useUpdateRecords() {
  return useMutation({
    mutationFn: (data: { business: string; update: RecordsUpdate }) => {
      return updateRecords(data.business, data.update);
    },
  });
}
