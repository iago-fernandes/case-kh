from airflow.models.baseoperator import BaseOperator
from common.gcs_storage import get_data, store_data
import pandas as pd
import io
from datetime import datetime


class ReceitasOperator(BaseOperator):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
    def execute(self, context):
        
        # INGESTÃO
        bucket_name = 'case-kh'
        get_file_path = 'files/gdvReceitasExcel.csv'
        
        csv_data = get_data(bucket_name, get_file_path)
        
        df = pd.read_csv(io.BytesIO(csv_data), encoding='ISO-8859-1')
        
        
        # TRANSFORMAÇÕES
        data_atual = datetime.now()
        
        df = df[['Fonte de Recursos', 'Receita', 'Arrecadado']]
        df = df.drop(df.index[-1])
        df[['ID Fonte Recurso', 'Fonte de Recursos']] = df['Fonte de Recursos'].str.split(' - ', n=1, expand=True)
        df = df[['ID Fonte Recurso', 'Fonte de Recursos', 'Receita', 'Arrecadado']]
        df['Arrecadado'] = df['Arrecadado'].str.strip()
        df['Arrecadado'] = df['Arrecadado'].str.replace('.', '').str.replace(',', '.').astype(float)
        df = df.rename(columns=lambda x: x.strip().lower().replace(' ', '_'))
        df['dt_insert'] = data_atual
        
        # ARMAZENAMENTO
        data = data_atual.date()
        hora = data_atual.hour
        minuto = data_atual.minute
        
        store_file_path = f'data/receitas/dt_ingestion={data}/{hora}/{minuto}/receitas.csv'
        
        csv_data_store = df.to_csv(index=False)
        
        store_data(bucket_name, store_file_path, csv_data_store)