import { format, isValid } from "date-fns";

export const renderDate = (dateStr?: string) => {
  const date = new Date(dateStr);
  if (!!date && isValid(date)) {
    return format(date, "dd/MM/yyyy");
  }
  return undefined;
};
