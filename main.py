# This is a sample Python script.
import requests, json
import pandas as pd
import variables
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_data(databaseId,secret_key):
    api_url = f"https://api.notion.com/v1/databases/{databaseId}/query"
    request_headers = {
        "Authorization": "Bearer {}".format(secret_key),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"}
    res = requests.request("POST", api_url, headers=request_headers)
    print(res.status_code)
    data = res.json()
    df = process_data(data)
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return df

def process_data(json):
    results = json["results"]
    plain_types = ["number","files","multi_select"]
    array_types = ["formula","select"]
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
            entry[name] = value
        list_.append(entry)
    df = pd.DataFrame(list_)
    return df


    #df = pd.DataFrame(fields)
    #return df



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    token = variables.token
    database_id = variables.database_id
    df = get_data(database_id,token)
    df.to_csv("output.csv")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
