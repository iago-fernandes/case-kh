def cotacao_query_silver():
    
    cotacao_query = """
    
    CREATE OR REPLACE TABLE `fake-api-424117.case_kh_silver.cotacao` 
    AS
    WITH latest_date_cte AS (
      SELECT MAX(dt_ingestion) AS latest_date
      FROM `fake-api-424117.case_kh_bronze.cotacao`
    )
    SELECT 
      code,
      codein,
      name,
      high,
      create_date,
      dt_insert
    FROM `fake-api-424117.case_kh_bronze.cotacao`
    WHERE dt_ingestion = (SELECT latest_date FROM latest_date_cte);
    
    """
    
    return cotacao_query