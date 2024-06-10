def cotacao_query_bronze():
    
    cotacao_query = """
    
    CREATE OR REPLACE EXTERNAL TABLE fake-api-424117.case_kh_bronze.cotacao (
      code STRING,
      codein STRING,
      name STRING,
      high FLOAT64,
      create_date DATETIME,
      dt_insert DATETIME
    )
    WITH PARTITION COLUMNS(
      dt_ingestion DATE
    )
    OPTIONS (
      format = 'CSV',
      skip_leading_rows = 1,
      uris = ['gs://case-kh/data/cotação/*'],
      hive_partition_uri_prefix = 'gs://case-kh/data/cotação'
    );
    """
    
    return cotacao_query