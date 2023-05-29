import boto3
import botocore.exceptions
import json
from .utils import get_image_creation_date, create_http_response

def v1_vision(event, context):

    request_body = json.loads(event['body'])
    bucket = request_body['bucket']
    imageName = request_body['imageName']
    url_to_image = f"https://{bucket}/{imageName}"
    
    # Verificar se a imagem existe no bucket
    s3 = boto3.client('s3')
    try:
        s3.head_object(Bucket=bucket, Key=imageName)

    except botocore.exceptions.ClientError as e:
        # Imagem não encontrada no bucket
        error_message = "Imagem não encontrada no bucket."
        response = create_http_response(500, {"error": error_message})
        return response
    
    # Conecta-se ao AWS Rekognition e seleciona o serviço de reconhecimento de rótulos
    rekognition = boto3.client('rekognition')
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': imageName
            }
        }
    )

    # Extrai os rótulos e confiança associada. Apenas os 4 primeiros rótulos serão mostrados
    labels = []
    for label in response['Labels'][:4]:  
        labels.append({
            'Name': label['Name'],
            'Confidence': label['Confidence']
        })

    result = {
        'url_to_image': url_to_image,
        'created_image': get_image_creation_date(bucket, imageName),
        'labels': labels
    }

    #Imprime o resultado nos logs do CloudWatch
    print(result)

    return create_http_response(200, result)

