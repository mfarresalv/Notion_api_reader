# Notion api reader

This will connect to a Notion database, and download all its rows. So far is only downloading as a csv, however, eventually it will upload the csv into google drive or specific google sheets. 
The purpose is to make a automatic process to update a google sheets based on Notion.

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
