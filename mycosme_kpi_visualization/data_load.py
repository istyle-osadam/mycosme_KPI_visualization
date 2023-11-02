import google.cloud.bigquery.magics
google.cloud.bigquery.magics.context.use_bqstorage_api = True
	
from google.cloud import bigquery
from google.cloud import bigquery_storage

import pandas as pd

GCP_PROJECT = "ml-development-344502"

bq_client = bigquery.Client(project=GCP_PROJECT)
bqstorage_client = bigquery_storage.BigQueryReadClient()

# f = open('mycosme_KPI_visualization/mycosme_kpi_visualization/request_sql.txt', 'r', encoding='UTF-8')
# data = f.read()
# QUERY = (data)
# query_job = bq_client.query(QUERY)  # API request
# rows = query_job.result()  # Waits for query to finish
# f.close()
# for row in rows:
#     print(row)ß

# df = bq_client.query(data).to_dataframe()
# print(df.columns)

def get_data():
    GCP_PROJECT = "ml-development-344502"

    bq_client = bigquery.Client(project=GCP_PROJECT)
    bqstorage_client = bigquery_storage.BigQueryReadClient()

    f  = open('mycosme_KPI_visualization/mycosme_kpi_visualization/request_sql.txt', 'r', encoding='UTF-8') 
    data = f.read()
    QUERY = (data)
    query_job = bq_client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish
    f.close()

    df = bq_client.query(data).to_dataframe()
    return df