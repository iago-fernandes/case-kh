from datetime import datetime, timedelta
from airflow import DAG
from bronze.receitas.receitas import ReceitasOperator
from bronze.receitas.external_table import receitas_query_bronze
from silver.receitas import receitas_query_silver
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
    'receitas',
    default_args=default_args,
    description='Ingestão e armazenamento de dados de receitas do arquivo .csv no GCS.',
    schedule_interval=timedelta(days=1),
)


bronze_receitas = ReceitasOperator(
    task_id='bronze_receitas',
    dag=dag
)

receitas_external_table = BigQueryExecuteQueryOperator(
    task_id='receitas_external_table',
    sql=receitas_query_bronze(),
    use_legacy_sql=False,
    gcp_conn_id='google_cloud_conn',
    location='us-east1',
    dag=dag
)

receitas_silver = BigQueryExecuteQueryOperator(
    task_id='receitas_silver',
    sql=receitas_query_silver(),
    use_legacy_sql=False,
    gcp_conn_id='google_cloud_conn',
    location='us-east1',
    dag=dag
)

bronze_receitas >> receitas_external_table >> receitas_silver

