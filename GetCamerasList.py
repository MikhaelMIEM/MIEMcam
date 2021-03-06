from googleapiclient.discovery import build
from google.oauth2 import service_account

def getCamerasList():
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.resource.calendar.readonly',
                  'https://www.googleapis.com/auth/admin.directory.resource.calendar']
    SERVICE_ACCOUNT_FILE = 'visca-onvif-converter-20020854b334.json'
    with open('gsuit_domain_account.txt') as file:
        GSUIT_DOMAIN_ACCOUNT = file.readline()

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(GSUIT_DOMAIN_ACCOUNT)
    service = build('admin', 'directory_v1', credentials=delegated_credentials)
    results = service.resources().calendars().list(customer='C03s7v7u4').execute()
    cameras = []
    for i in results['items']:
        if i['resourceType'] == 'ONVIF-camera':
            cameras.append(i)
    return cameras