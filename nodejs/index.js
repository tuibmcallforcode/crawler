import { fetchRelieftWeb } from "./utils/reliefWebControllers";

const option = {
    "offset" :  0,
    "query": {
        "value": "earthquake"
    },
    "profile":  "list",
    "limit"  :  100,
    "sort"   :  ["date:desc"]
}

fetchRelieftWeb(option);
