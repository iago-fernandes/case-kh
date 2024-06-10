# Case Karhub

## Descrição
O desafio consiste em desenvolver um ETL para processar arquivos que representam o orçamento do Estado de São Paulo de 2022 e armazená-los em um formato consistente para responder perguntas que ajudarão nosso time.

## Índice
9. [Arquitetura do Projeto](#arquitetura-do-projeto)
9. [Tecnologias Utilizadas](#tecnologias-utilizadas)
1. [Preparação do ambiente local](#ambiente)
2. [Instalação do airflow](#airflow)
3. [Ingestão dos dados](#ingestão)
4. [Estrutura de diretórios no GCS](#estrutura-de-diretórios-no-gcs)
4. [Criação de tabelas externas no Big Query](#criação-de-tabelas-externas-no-big-query)
5. [Criação da camada de dados Silver](#criação-da-camada-de-dados-silver)
6. [Criação da tabela final](#criação-da-tabela-final)
7. [Criação das DAGs de orquestração](#criação-das-dags-de-orquestração)
8. [Perguntas finais](#perguntas-finais)

