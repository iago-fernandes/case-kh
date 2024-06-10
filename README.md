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

## Tecnologias Utilizadas
- Python (Pandas)
- SQL
- Apache Airflow
- Google Cloud Storage
- Big Query

## Preparação do Ambiente Local

Para ativar o ambiente virtual, utilize o comando

```sh
pipenv shell
```

## Instalação do Airflow

Instale o Docker Desktop, ele instala o Docker Compose junto por padrão.

Crie um arquivo .yml para as configurações do Airflow local com o conteúdo do arquivo ARQUIVO_YML_EXEMPLO, armazene o arquivo no diretório do projeto. Certifique-se de substituir o campo 'YOUR_FERNET_KEY' no arquivo .yml por uma chave fernet, que pode ser gerada pelo seguinte comando:

```sh
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Em seguida, inicie os containers com o comando:

```sh
docker-compose up -d
```

Então instale o airflow e seu componente para o google com:

```sh
pipenv install apache-airflow apache-airflow-providers-google
```

O Airflow irá criar três diretórios dentro da pasta do projeto:

- dags
- logs
- plugins

Assim como nesse repositório, todos arquivos devem ficar dentro da pasta dags, que é o local onde o airflow executa.

## Ingestão dos dados

Os dados são consumidos e armazenados por meio do módulo 'gcs_storage.py' que pode ser encontrado em 'dags/common'. O arquivo segredo json da conta de serviço deve ser colocado em 'dags/arquivo_segredo.json'.

O diretório 'dags/bronze' contém os arquivos .py que realizam as transformações necessárias dos dados para cada fonte de dados e são eles:

- dags/bronze/cotação/cotação.py
- dags/bronze/despesas/despesas.py
- dags/bronze/receitas/receitas.py

O armazenamento dos dados dentro do GCS segue o seguinte layout:

'data/despesas/dt_ingestion={data}/{hora}/{minuto}/despesas.csv'

Onde a data de ingestão é gerada a cada ciclo de execução.

## Estrutura de diretórios no GCS

A estruturação dos diretórios dentro do Data Lake fica da seguinte forma:

AQUI UMA IMAGEM COM A ESTRUTURA DE PASTAS DENTRO DO GCS

## Criação de tabelas externas no Big Query

A criação de tabelas externas particionadas no Big Query é feita pelos arquivos .py:

- dags/bronze/cotação/external_table.py
- dags/bronze/despesas/external_table.py
- dags/bronze/receitas/external_table.py

O particionamento das tabelas é feito pela data de ingestão dos dados seguinto o formato:

'dt_ingestion=YYYY-mm-dd'

COLOCAR IMAGEM DAS TABELAS NO BIG QUERY

## Criação da camada de dados Silver

A camada de dados Silver é responsável por consumir a camada bronze e salvar apenas os dados mais recentes baseado na data de particionamento da tabela externa 'dt_ingestion'

Os arquivos com as querys de criação das tabelas podem ser encontrados em:

- dags/silver/cotacao.py
- dags/silver/despesas.py
- dags/silver/receitas.py

COLOCAR IMAGEM DAS TABELAS SILVER NO BIG QUERY

## Criação da tabela final

O arquivo com a query para a construção da tabela final com valores agregados, aqui considerada como camada Gold, pode ser encontrado em:

- dags/gold/valores_totais_real.py

COLOCAR IMAGEM DA TABELA NO BIG QUERY


## Criação das DAGs de orquestração

As DAGs para execução do fluxo de orquestração podem ser encontradas em:

- dags/dag_bag

OBS.: A configuração da conexão do Airflow com o provedor Google é feita a partir do console do Airflow em 'Admin > Connections', esse id é passado como o parâmetro 'gcp_conn_id' na construção da DAG.

## Perguntas finais

As querys para a contrução das respostas das perguntas são encontradas em:

- dags/perguntas_finais/perguntas_finais.sql

As respostas estão a seguir:

Quais são as 5 fontes de recursos que mais arrecadaram?

| id_fonte_recurso | nome_fonte_de_recurso | total_arrecadado_reais |
|----------|----------|----------|
| 001   | TESOURO-DOT.INICIAL E CRED.SUPLEMENTAR | 755199899144.41 |
| 002  | RECURSOS VINCULADOS ESTADUAIS | 269320418872.57 |
| 081  | TESOURO-DOT.INICIAL E CRED.SUPLEMENTAR-INTRA | 160784649176.57 |
| 004  | REC.PROPRIO-ADM.IND.-DOT.INIC.CR.SUPL. | 56521380942.44 |
| 005  | RECURSOS VINCULADOS FEDERAIS | 44605319221.94 |

Quais são as 5 fontes de recursos que mais gastaram?


Quais são as 5 fontes de recursos com a melhor margem bruta?


Quais são as 5 fontes de recursos que menir arrecadaram?


Quais são as 5 fontes de recursos que menir gastaram?


Quais são as 5 fontes de recursos com a pior margem bruta?


Qual a média de arrecadação por fonte de recurso?


Qual a média de gastos por fonte de recurso?

