def despesas_query_silver():
    
    despesas_query = """
    
    CREATE OR REPLACE TABLE `fake-api-424117.case_kh_silver.despesas` 
    AS
    WITH latest_date_cte AS (
      SELECT MAX(dt_ingestion) AS latest_date
      FROM `fake-api-424117.case_kh_bronze.despesas`
    )
    SELECT 
      id_fonte_recurso,
      fonte_de_recursos,
      despesa,
      liquidado,
      dt_insert
    FROM `fake-api-424117.case_kh_bronze.despesas`
    WHERE dt_ingestion = (SELECT latest_date FROM latest_date_cte);
    
    """
    
    return despesas_query