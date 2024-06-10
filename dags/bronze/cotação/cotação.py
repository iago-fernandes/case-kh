from airflow.models.baseoperator import BaseOperator
import requests
import pandas as pd
from common.gcs_storage import store_data
from datetime import datetime

class CotacaoOperator(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


    def execute(self, context):
        
        # INGESTÃO
        url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL?start_date=20220622&end_date=20220622"
        
        response = requests.get(url)
        
        if response.status_code == 200:
           data = response.json()
           
        else:
           print("Erro ao obter os dados:", response.status_code)
    
        
        # TRANSFORMAÇÕES
        data_atual = datetime.now()
        
        df = pd.DataFrame(data)
        df = df[['code', 'codein', 'name', 'high', 'create_date']]
        df['dt_insert'] = data_atual
        
        
        # ARMAZENAMENTO
        bucket_name = 'case-kh'
        
        data = data_atual.date()
        hora = data_atual.hour
        minuto = data_atual.minute
        
        store_file_path = f'data/cotação/dt_ingestion={data}/{hora}/{minuto}/cotação.csv'
        
        csv_data = df.to_csv(index=False)
        
        store_data(bucket_name, store_file_path, csv_data)