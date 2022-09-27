from google.cloud import bigquery
import os
from shared_code.set_adls import initialize_storage_account
from shared_code.set_bigquery import initialize_bq
from shared_code.parse_download import bytes_to_df

def adls_to_bq(container, directory, customer_name):

    # Initialize ADLS client and point to correct directory where files reside
    service_client = initialize_storage_account()
    file_system_client = service_client.get_file_system_client(file_system=container)
    directory_client = file_system_client.get_directory_client(directory=directory)
    paths = file_system_client.get_paths(path=directory)

    # Initialize Big Query client
    bq_client = initialize_bq(customer_name)

    customer_dataset_name = customer_name + '_DATASET_NAME'
    dataset_name = os.environ[customer_dataset_name]
    dataset_ref = bq_client.dataset(dataset_name)

    customer_dataset_id = customer_name + '_DATASET_ID'
    bq_dataset_id = os.environ[customer_dataset_id]

    # Iterate over all files in directory and load into a dataframe
    for file in paths:
        file_name = file.name.split('/', 1)[-1]
        file_client = directory_client.get_file_client(file_name)
        download = file_client.download_file().readall()
        df = bytes_to_df(download)

        print('file: ', file)
        # print('df.head: ', df.head())
        # Create table if doesn't exist
        table_name = file_name.split('.')[0].lower()
        table_id = f"{bq_dataset_id}.{table_name}"
        bq_client.create_table(table_id, exists_ok=True)

        print('table name: ', table_name)
        print('table_id: ', table_id)
        # Big Query Config to Truncate Load table
        table_ref = dataset_ref.table(table_name)
        job_config = bigquery.LoadJobConfig()
        job_config.source_format = bigquery.SourceFormat.CSV
        job_config.write_disposition = 'WRITE_TRUNCATE'
        job_config.autodetect = True

        job = bq_client.load_table_from_dataframe(df, table_ref, job_config=job_config)

        table = bq_client.get_table(table_id)

        print(
            "Loaded {} rows and {} columns to {}".format(
                table.num_rows, len(table.schema), table_id
            )
        )

    print('DONE')