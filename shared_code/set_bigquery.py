import os
from google.cloud import bigquery
from google.oauth2 import service_account

def initialize_bq(customer_name):
    config_file_name = customer_name + '_KEY_PATH'
    key_path = os.environ[config_file_name]
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    return client