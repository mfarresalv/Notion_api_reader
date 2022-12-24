# This is a sample Python script.
import requests, json
import pandas as pd
import variables
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
    list_ = []

    for row in results:
        fields = row["properties"]
        entry = {}
        for column in fields:
            fname, fvalue = process_datatypes(fields,column)
            entry[fname] = fvalue
        list_.append(entry)
    df = pd.DataFrame(list_)
    df["Fecha esperada"]=df["Fecha esperada"].astype("datetime64[ns]")
    df["Fecha real"] = df["Fecha real"].astype("datetime64[ns]")
    df["Next due"] = df["Next due"].astype("datetime64[ns]")
    df["Fecha creación"] = df["Fecha creación"].astype("datetime64[ns]")
    return df

def process_datatypes(json:str,column:str,more_entries=True):
    """
    returns each field and value idividually

    """
    name = column
    ctype = json[column]["type"]
    value = json[column][ctype]
    if ctype == "title":
        title_type = value[0]["type"]
        name = "name"
        value = value[0][title_type]["content"]
        more_entries = False
    elif type(value) != dict:
        value = json[column][ctype]
        more_entries = False
    while more_entries:
        if ctype=="select":
            value = value["name"]
        elif ctype=="date":
            value=value["start"]
        else:
            ntype = value["type"]
            value = value[ntype]
        if type(value) != dict:
            more_entries = False
        else:
            ctype=ntype
    return name, value



if __name__ == '__main__':
    token = variables.token
    database_id = variables.database_id
    df = get_data(database_id,token)
    df.to_csv("/Users/miquelfarre/Google Drive/Mi unidad/scripts-gsheets/piso_recurrentes.csv")



