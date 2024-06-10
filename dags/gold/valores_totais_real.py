def valores_totais_real_query():
    
    valores_totais_query = """
    
    CREATE OR REPLACE TABLE `fake-api-424117.case_kh_gold.valores_totais_real`
    AS
    WITH total_despesas
    AS (
      SELECT
        id_fonte_recurso,
        fonte_de_recursos,
        SUM(liquidado) AS total_liquidado
      FROM 
        `fake-api-424117.case_kh_silver.despesas`
      GROUP BY
        id_fonte_recurso,
        fonte_de_recursos
    ),
    total_receitas
    AS (
      SELECT 
        id_fonte_recurso,
        fonte_de_recursos,
        SUM(arrecadado) AS total_arrecadado
      FROM 
        `fake-api-424117.case_kh_silver.receitas`
      GROUP BY
        id_fonte_recurso,
        fonte_de_recursos
    ),
    cotacao_atual
    AS (
      SELECT
        high AS cotacao
      FROM
        `fake-api-424117.case_kh_silver.cotacao`
    )
    SELECT
      td.id_fonte_recurso,
      td.fonte_de_recursos AS nome_fonte_de_recurso,
      (td.total_liquidado * (SELECT cotacao FROM cotacao_atual)) AS total_liquidado_reais,
      (tr.total_arrecadado * (SELECT cotacao FROM cotacao_atual)) AS total_arrecadado_reais,
    FROM
      total_despesas td
    LEFT JOIN
      total_receitas tr
    ON
      td.id_fonte_recurso = tr.id_fonte_recurso
    ORDER BY
      td.id_fonte_recurso;
    
    """
    
    return valores_totais_query