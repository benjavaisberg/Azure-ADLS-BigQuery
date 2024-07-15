import logging

import azure.functions as func
from shared_code.adls_to_bq import write_to_bq


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    req_body = req.get_json()

    container =  req_body['container']
    directory = req_body['directory']
    bq_project = req_body['bq_project']
    bq_dataset =  req_body['bq_dataset']
    bq_table = req_body['bq_table']

    write_to_bq(
        container=container,
        directory=directory,
        bq_project=bq_project,
        bq_dataset=bq_dataset,
        bq_table=bq_table
    )


    return func.HttpResponse(
            "SUCCESS. ADDED INVENTORY TO BIGQUERY",
            status_code=200
    )
