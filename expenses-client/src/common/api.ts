import { StatsModel } from "./models";
import { useQuery } from "react-query";
import httpClient from "./httpClient";

async function getStats() {
  const { data } = await httpClient.get<StatsModel>("/statistics");
  return data;
}

export function useGetStates() {
  return useQuery(["stats"], getStats);
}
