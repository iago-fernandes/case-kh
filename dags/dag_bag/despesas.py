from datetime import datetime, timedelta
from airflow import DAG
from bronze.despesas.despesas import DespesasOperator
from bronze.despesas.external_table import despesas_query_bronze
from silver.despesas import despesas_query_silver
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
    'despesas',
    default_args=default_args,
    description='Ingestão e armazenamento de dados de despesas do arquivo .csv no GCS.',
    schedule_interval=timedelta(days=1),
)


bronze_despesas = DespesasOperator(
    task_id='bronze_despesas',
    dag=dag
)

despesas_external_table = BigQueryExecuteQueryOperator(
    task_id='despesas_external_table',
    sql=despesas_query_bronze(),
    use_legacy_sql=False,
    gcp_conn_id='google_cloud_conn',
    location='us-east1',
    dag=dag
)

despesas_silver = BigQueryExecuteQueryOperator(
    task_id='despesas_silver',
    sql=despesas_query_silver(),
    use_legacy_sql=False,
    gcp_conn_id='google_cloud_conn',
    location='us-east1',
    dag=dag
)

bronze_despesas >> despesas_external_table >> despesas_silver

