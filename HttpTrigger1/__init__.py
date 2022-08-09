import logging
import azure.functions as func
from shared_code.adls_to_bq import adls_to_bq

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    container = req.params.get('container')
    directory = req.params.get('directory')
    if not container:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            container = req_body.get('container')
            directory = req_body.get('directory')

    if container and directory:
        adls_to_bq(container=container, directory=directory)

        return func.HttpResponse(
             "Added data to BigQuery tables",
             status_code=200
        )
