def receitas_query_bronze():
    receitas_query = """
    
    CREATE OR REPLACE EXTERNAL TABLE fake-api-424117.case_kh_bronze.receitas (
      id_fonte_recurso STRING,
      fonte_de_recursos STRING,
      receita STRING,
      arrecadado FLOAT64,
      dt_insert DATETIME
    )
    WITH PARTITION COLUMNS(
      dt_ingestion DATE
    )
    OPTIONS (
      format = 'CSV',
      skip_leading_rows = 1,
      uris = ['gs://case-kh/data/receitas/*'],
      hive_partition_uri_prefix = 'gs://case-kh/data/receitas'
    );
    
    """
    
    return receitas_query