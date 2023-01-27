# Notion api reader

This script connects to a Notion Database (given a Notion auth token and a id of a database), and downloads it into a local file (directory path of outcome must be given). After downloading the file, the script replaces one existing given csv file in google drive with the downloaded data (note that the script do not create the file. The file need to exist, even if it is in blank)

## Auth and config
Need to create access key on notion, and grant access to notion database. See urls to know how to do it.

### Google auth

Need to create a service account on google cloud console, give acces to that account to the google drive document that we want to replace. Create a key related to that service account and save it in the same repository with this name `google_drive_key.json`

Here is the documentation on how to create a service account: https://cloud.google.com/iam/docs/creating-managing-service-accounts?hl=es-419



### Inputs

Via enviroment variables:
- `TOKEN`: Notion token
- `DBID`: Notion database_id
- `OUT_DIR`: Directory path where the outcome csv is stored 
- `GDRIVE_FILE_ID`: The id from the existing file on google drive, the process of the script will replace that file with the new data.

Other inputs:
- `google_drive_key.json`: the authentication json provided by google in order to access the service account.

check this to find `database_id` : https://developers.notion.com/docs/working-with-databases

Notion API documentation : https://developers.notion.com/docs/authorization 

## Compatible Notion fields

* Number
* Files (not tested)
* Multi_select (not tested)
* Select
* Date (start dates)
* formula
  * boolean
  * date (only start dates)

## Executing on command line
Will need to install all dependencies, and then execute the next bash command with all the enviroment variables listed before setled up, here an example
```console
TOKEN="secret_xxxxxxxxx" DBID="xxxxxxxxxx" OUT_DIR="xxxxx.csv" GDRIVE_FILE_ID="xxxxxx" python main.py
```
## Executing on docker

Need to have docker installed on the machine, after that, Run this bash command to create the image. 
```console
docker build -t notion_api_reader .
```
This can also be done by executing the next:
```console
bash docker_image_build.sh
```
Once the image is created, need to run the `docker run` command with all the enviroment variables descripted above
```console
docker run -e TOKEN=secret_xxxxxxxx -e DBID=xxxxxxxx -e OUT_DIR=/outputs/piso_recurrentes.csv -e GDRIVE_FILE_ID=xxxxx notion_api_reader
```
