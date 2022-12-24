# This is a sample Python script.
import requests, json
import pandas as pd
import os
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_data(databaseId:str,secret_key:str,export_json:bool=False)->pd.DataFrame:
    """
    Reads data from a specified Notion database and returns it as a pandas Dataframe.

    Args:
    databaseId (str): database id, extracted from notion
    secret_key: Secret key on Notion account, to grant access
    export_json: If set true, it will generate a JSON with http response

    """
    api_url = f"https://api.notion.com/v1/databases/{databaseId}/query"
    request_headers = {
        "Authorization": "Bearer {}".format(secret_key),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"}
    res = requests.request("POST", api_url, headers=request_headers)
    print(res.status_code)
    data = res.json()
    df = process_data(data)
    if export_json:
        with open('./db.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)
    return df

def process_data(json:str)->pd.DataFrame:
    """
    Gets the JSON data from the api response, and transforms it into a dataframe

    Args
    json: the raw data directly given by Notion API
    """
    results = json["results"]
    plain_types = ["number","files","multi_select"]
    array_types = ["formula","select","date"]
    list_ = []

    for row in results:
        fields = row["properties"]
        entry = {}
        for column in fields:
            name = column
            type = fields[column]["type"]
            if type=="title":
                title_type = fields[column][type][0]["type"]
                name = "name"
                value = fields[column][type][0][title_type]["content"]
            if type in plain_types:
                value = fields[column][type]
            if type in array_types:
                if type == "formula":
                    sub_type = fields[column][type]["type"]
                    if sub_type == "boolean":
                        value = fields[column][type][sub_type]
                    if sub_type == "date":
                        value = fields[column][type][sub_type]["start"]
                if type == "select":
                    value = fields[column][type]["name"]
                if type == "date":
                    if fields[column][type]:
                        value = fields[column][type]["start"]
                    else:
                        value = None
            entry[name] = value
        list_.append(entry)
    df = pd.DataFrame(list_)
    return df


def main():
    token = os.environ.get("TOKEN")
    database_id = os.environ.get("DBID")
    df = get_data(database_id, token)
    df.to_csv("/Users/miquelfarre/Google Drive/Mi unidad/scripts-gsheets/piso_recurrentes.csv")

if __name__ == '__main__':
    main()



