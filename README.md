# Notion api reader

The file `main.py` connects to a Notion Database (given a Notion auth token and a id of a database), and downloads it into a local file (it coluld be a google drive directory using google drive app). 

## Auth and config
Need to create access key on notion, and grant access to notion database.

### Inputs

Via enviroment variables:
- `TOKEN`: Notion token
- `DBID`: Notion database_id

check this to find `database_id` : https://developers.notion.com/docs/working-with-databases

Notion API documentation : https://developers.notion.com/docs/authorization

## Compatible fields

* Number
* Files (not tested)
* Multi_select (not tested)
* Select
* Date (start dates)
* formula
  * boolean
  * date (only start dates)
