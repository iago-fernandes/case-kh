from datetime import datetime, timedelta
from airflow import DAG
from bronze.cotação.cotação import CotacaoOperator
from bronze.cotação.external_table import cotacao_query_bronze
from silver.cotacao import cotacao_query_silver
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator


default_args = {
    'owner': 'karhub',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 6, 9),
}


dag = DAG(
    'cotação',
    default_args=default_args,
    description='Ingestão e armazenamento de dados da API de cotação USD-BRL.',
    schedule_interval=timedelta(days=1),
)


bronze_cotacao = CotacaoOperator(
    task_id='bronze_cotacao',
    dag=dag
)

cotacao_external_table = BigQueryExecuteQueryOperator(
    task_id='cotacao_external_table',
    sql=cotacao_query_bronze(),
    use_legacy_sql=False,
    gcp_conn_id='google_cloud_conn',
    location='us-east1',
    dag=dag
)

cotacao_silver = BigQueryExecuteQueryOperator(
    task_id='cotacao_silver',
    sql=cotacao_query_silver(),
    use_legacy_sql=False,
    gcp_conn_id='google_cloud_conn',
    location='us-east1',
    dag=dag
)

bronze_cotacao >> cotacao_external_table >> cotacao_silver

