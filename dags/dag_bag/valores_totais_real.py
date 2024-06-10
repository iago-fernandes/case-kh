from datetime import datetime, timedelta
from airflow import DAG
from gold.valores_totais_real import valores_totais_real_query
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
    'gold_valores_totais_real',
    default_args=default_args,
    description='Tabela agregada com valores totais em para receita e despesas em real.',
    schedule_interval=timedelta(days=1),
)



valores_totais_real = BigQueryExecuteQueryOperator(
    task_id='valores_totais_real',
    sql=valores_totais_real_query(),
    use_legacy_sql=False,
    gcp_conn_id='google_cloud_conn',
    location='us-east1',
    dag=dag
)

valores_totais_real

