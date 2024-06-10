def receitas_query_silver():
    
    receitas_query = """
    
    CREATE OR REPLACE TABLE `fake-api-424117.case_kh_silver.receitas` 
    AS
    WITH latest_date_cte AS (
      SELECT MAX(dt_ingestion) AS latest_date
      FROM `fake-api-424117.case_kh_bronze.receitas`
    )
    SELECT 
      id_fonte_recurso,
      fonte_de_recursos,
      receita,
      arrecadado,
      dt_insert
    FROM `fake-api-424117.case_kh_bronze.receitas`
    WHERE dt_ingestion = (SELECT latest_date FROM latest_date_cte);
    
    """
    
    return receitas_query