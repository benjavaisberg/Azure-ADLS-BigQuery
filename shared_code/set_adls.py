import os
from azure.storage.filedatalake import DataLakeServiceClient

def initialize_storage_account():
    
    storage_account_name = os.environ['STORAGE_ACCOUNT_NAME']
    storage_account_key =  os.environ['STORAGE_ACCOUNT_KEY']
    try:
        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=storage_account_key)
    
    except Exception as e:
        print(e)
        
    return service_client