import { RecordsModel, RecordsSelection, StatsModel } from "./models";
import { useQuery } from "react-query";
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
