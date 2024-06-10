from google.cloud import storage
import json
        
def get_data(bucket_name, source_blob_path):
    
    try:
        client = storage.Client.from_service_account_json('dags/fake-api-424117-ae150130f88f.json')
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(source_blob_path)
        data = blob.download_as_bytes()
        
        print(f"Blob {source_blob_path} baixado.")
        
        return data
        
    except Exception as e:
        print(f"Erro ao baixar arquivo: {e}")
        

def store_data(bucket_name, file_path, csv_data):
    
    try:
    
        client = storage.Client.from_service_account_json('dags/fake-api-424117-ae150130f88f.json')
        
        bucket = client.get_bucket(bucket_name)
        
        blob = bucket.blob(file_path)
        
        blob.upload_from_string(
            csv_data,
            content_type='text/csv'
            )
        
        print(f'Arquivo salvo como {file_path} no bucket {bucket_name}')
        
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        