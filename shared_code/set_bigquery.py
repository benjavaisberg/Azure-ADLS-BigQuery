import os
from google.cloud import bigquery
from google.oauth2 import service_account

def initialize_bq():
    key_path = os.environ['KEY_PATH']
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    return client