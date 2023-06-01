from google.cloud import bigquery
import os
from shared_code.set_adls import initialize_storage_account
from shared_code.set_bigquery import initialize_bq
from shared_code.parse_download import bytes_to_df
from google.cloud.exceptions import NotFound
import logging
import schema.captiva_schema

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

    # Define schemas
    deliveries_by_date_schema = schema.captiva_schema.deliveries_by_date_schema
    receipt_resin_preforms_schema = schema.captiva_schema.receipt_resin_preforms_schema
    warehouse_transfers_schema = schema.captiva_schema.warehouse_transfers_schema
    sales_orders_forecast_schema = schema.captiva_schema.sales_order_forecast_schema

    schema_dict = {'deliveries_by_date': deliveries_by_date_schema,
                   'receipt_resin_preforms': receipt_resin_preforms_schema,
                   'warehouse_transfers': warehouse_transfers_schema,
                   'sales_orders_forecast': sales_orders_forecast_schema}


    # Iterate over all files in directory and load into a dataframe
    for file in paths:
        file_name = file.name.split('/', 1)[-1]
        file_client = directory_client.get_file_client(file_name)

        download = file_client.download_file().readall()
        df = bytes_to_df(download)

        df = df.replace(r'\n',' ', regex=True)
        df = df.replace(r'\r',' ', regex=True)

        logging.info('==============================================================================================================================================')
        
        table_name = file_name.split('.')[0].lower()
        table_id = f"{bq_dataset_id}.{table_name}"

        # Check if table already exists. If not, go ahead and create it.
        try:
            table = bq_client.get_table(table_id)
            logging.info("Table {} already exists.".format(table_id))
        except NotFound:
            logging.info("Table {} is not found. Creating now...".format(table_id))
            table = bigquery.Table(table_id, schema=schema_dict[table_name])
            table = bq_client.create_table(table, exists_ok=True)
            logging.info("Created table {} ".format(table_id))

        # Big Query Config to Truncate Load table
        table_ref = dataset_ref.table(table_name)
        job_config = bigquery.LoadJobConfig()
        job_config.source_format = bigquery.SourceFormat.CSV
        job_config.write_disposition = 'WRITE_TRUNCATE'
        job_config.schema = schema_dict[table_name]
        job_config.allow_quoted_newlines = True

        job = bq_client.load_table_from_dataframe(df, table_ref, job_config=job_config)
        job.result()

        logging.info(
            "Loaded {} rows to {}".format(
                job.output_rows, job.destination
            )
        )

    logging.info('DONE')