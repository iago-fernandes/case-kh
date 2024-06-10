-- Quais sao as 5 fontes de recursos que mais arrecadaram?

SELECT
  id_fonte_recurso,
  nome_fonte_de_recurso,
  ROUND(total_arrecadado_reais, 2) AS total_arrecadado_reais
FROM `fake-api-424117.case_kh_gold.valores_totais_real`
ORDER BY
  total_arrecadado_reais DESC
LIMIT 5


-- Quais sao as 5 fontes de recursos que mais gastaram?

SELECT
  id_fonte_recurso,
  nome_fonte_de_recurso,
  ROUND(total_liquidado_reais, 2) AS total_liquidado_reais
FROM `fake-api-424117.case_kh_gold.valores_totais_real`
ORDER BY
  total_liquidado_reais DESC
LIMIT 5



-- Quais sao as 5 fontes de recursos com a melhor margem bruta?

SELECT
  id_fonte_recurso,
  nome_fonte_de_recurso,
  ROUND((total_arrecadado_reais - total_liquidado_reais) / NULLIF(total_arrecadado_reais, 0), 4) AS margem_bruta
FROM `fake-api-424117.case_kh_gold.valores_totais_real`
ORDER BY
  margem_bruta DESC
LIMIT 5



-- Quais sao as 5 fontes de recursos que menir arrecadaram?

SELECT
  id_fonte_recurso,
  nome_fonte_de_recurso,
  ROUND(total_arrecadado_reais, 2) AS total_arrecadado_reais
FROM `fake-api-424117.case_kh_gold.valores_totais_real`
ORDER BY
  total_arrecadado_reais ASC
LIMIT 5



-- Quais sao as 5 fontes de recursos que menir gastaram?

SELECT
  id_fonte_recurso,
  nome_fonte_de_recurso,
  ROUND(total_liquidado_reais, 2) AS total_liquidado_reais
FROM `fake-api-424117.case_kh_gold.valores_totais_real`
ORDER BY
  total_liquidado_reais ASC
LIMIT 5



-- Quais sao as 5 fontes de recursos com a pior margem bruta?


SELECT
  id_fonte_recurso,
  nome_fonte_de_recurso,
  ROUND((total_arrecadado_reais - total_liquidado_reais) / NULLIF(total_arrecadado_reais, 0), 4) AS margem_bruta
FROM `fake-api-424117.case_kh_gold.valores_totais_real`
ORDER BY
  margem_bruta ASC
LIMIT 5


-- Qual a media de arrecadacao por fonte de recurso?

SELECT
  id_fonte_recurso,
  fonte_de_recursos,
  AVG(arrecadado) AS media_arrecadacao
FROM `fake-api-424117.case_kh_silver.receitas`
GROUP BY
  id_fonte_recurso,
  fonte_de_recursos


-- Qual a media de gastos por fonte de recurso?

SELECT
  id_fonte_recurso,
  fonte_de_recursos,
  AVG(liquidado) AS media_liquidado
FROM `fake-api-424117.case_kh_silver.despesas`
GROUP BY
  id_fonte_recurso,
  fonte_de_recursos


