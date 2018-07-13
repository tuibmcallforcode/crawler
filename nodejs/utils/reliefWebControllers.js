import request from "request";
import fs      from "fs";
import path    from "path";

const API_URL = "https://api.reliefweb.int/v1/reports";
const FILE_PATH = path.join(__dirname, "..", "data/relief_data.json");

const writeToFile = ({filePath=FILE_PATH, data="", flag="w"}) => {
    return new Promise((resolve, reject) => { 
        fs.appendFile(filePath, data, { flag: flag }, err => {
            if(err) reject(err);
            else    resolve();
        });
    });
}

const _fetch = ({url=API_URL, method="GET", body={}}) => {
    return new Promise((resolve, reject) => {
        request(url, {
            method: method,
            body: JSON.stringify(body)
        }, (err, res, body) => {
            if(!err) resolve(JSON.parse(body));
            else     reject(err);
        });
    })
}

const fetchRelieftWeb = async () => {
    const options = {
        "offset" :  0,
        "profile":  "list",
        "limit"  :  5,
        "sort"   :  ["date:desc"]
    }
    const allReportQuery = {
        url: API_URL,
        method: "POST",
        body: options
    }

    try {
        const reportsResult = await _fetch(allReportQuery);
        reportsResult.data.forEach(async datum => {
            const datumDetails = await _fetch({url: datum.href});
            datum.fields = {
                ...datum.fields,
                ...datumDetails.data[0].fields
            };

            await writeToFile({data: JSON.stringify(datum)});
        });

    } catch (e) {
        console.log(`err: ${e}`);
    }

}

fetchRelieftWeb();