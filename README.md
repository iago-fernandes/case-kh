# Case Karhub

## Descrição
O desafio consiste em desenvolver um ETL para processar arquivos que representam o orçamento do Estado de São Paulo de 2022 e armazená-los em um formato consistente para responder perguntas que ajudarão nosso time.

## Índice
1. [Arquitetura do Projeto](#arquitetura-do-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Preparação do ambiente local](#ambiente)
4. [Instalação do airflow](#airflow)
5. [Ingestão dos dados](#ingestão)
6. [Estrutura de diretórios no GCS](#estrutura-de-diretórios-no-gcs)
7. [Criação de tabelas externas no Big Query](#criação-de-tabelas-externas-no-big-query)
8. [Criação da camada de dados Silver](#criação-da-camada-de-dados-silver)
9. [Criação da tabela final](#criação-da-tabela-final)
10. [Criação das DAGs de orquestração](#criação-das-dags-de-orquestração)
11. [Perguntas finais](#perguntas-finais)

