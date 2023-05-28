import boto3
import json
from .utils import get_image_creation_date

def v1_vision(event, context):
    request_body = json.loads(event['body'])
    bucket = request_body['bucket']
    imageName = request_body['imageName']
    url_to_image = f"https://{bucket}/{imageName}"
    
    # Conectar-se ao AWS Rekognition
    rekognition = boto3.client('rekognition')
    
    # Executar a detecção de rótulos na imagem
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': imageName
            }
        }
    )
    
    # Extrair os rótulos e confiança associada
    labels = []
    for label in response['Labels'][:4]:  # Apenas os 4 primeiros rótulos
        labels.append({
            'Name': label['Name'],
            'Confidence': label['Confidence']
        })
    
    result = {
        'url_to_image': url_to_image,
        'created_image': get_image_creation_date(bucket, imageName),
        'labels': labels
    }
    
    print(result)
    
    # Retornar uma resposta HTTP válida
    response = {
        'statusCode': 200,
        'body': json.dumps(result),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
        
    return response

