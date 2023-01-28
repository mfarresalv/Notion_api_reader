from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import variables as var

def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = service_account.Credentials.from_service_account_file(
    key_file_location)

    scoped_credentials = credentials.with_scopes(scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=scoped_credentials)

    return service


def replace_file_to_drive(file_id_replaced,file_replacement,key_file_location="google_drive_key.json"):
    '''Replace a given file in google drive, given the google drive file_id and the replacement

    Args:
        file_id_replaced: the id of the existing file on google drive
        file_replacement: the path of the file we want to upload 
        key_file_location: The path to a valid service account JSON key file.
    '''
    service = get_service(
            api_name='drive',
            api_version='v3',
            scopes=['https://www.googleapis.com/auth/drive'],
            key_file_location=key_file_location)
    service.files().update(
        fileId=file_id_replaced,
        media_body= file_replacement
    ).execute()
    
    pass

if __name__ == '__main__':
    main()