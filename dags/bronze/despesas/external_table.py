def despesas_query_bronze():
    despesas_query = """
    
    CREATE OR REPLACE EXTERNAL TABLE fake-api-424117.case_kh_bronze.despesas (
      id_fonte_recurso STRING,
      fonte_de_recursos STRING,
      despesa STRING,
      liquidado FLOAT64,
      dt_insert DATETIME
    )
    WITH PARTITION COLUMNS(
      dt_ingestion DATE
    )
    OPTIONS (
      format = 'CSV',
      skip_leading_rows = 1,
      uris = ['gs://case-kh/data/despesas/*'],
      hive_partition_uri_prefix = 'gs://case-kh/data/despesas'
    );
    
    
    """
    
    return despesas_query