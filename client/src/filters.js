import _ from "lodash";

export const isPrivate = s => _.startsWith(s, "_");

export const omitPrivate = o => _.omitBy(o, (value, key) => isPrivate(key));

export default {
  isPrivate,
  omitPrivate
};
