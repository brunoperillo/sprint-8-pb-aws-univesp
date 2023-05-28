import boto3
import json
from .utils import get_image_creation_date, create_http_response

def v1_vision(event, context):

    request_body = event.get('body')

    if request_body:
        request_body = json.loads(request_body)
        bucket = request_body.get('bucket')
        imageName = request_body.get('imageName')

        if bucket and imageName:
            url_to_image = f"https://{bucket}/{imageName}"

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

    # Requisição inválida
    error_message = {
            'error': 'ImageNotFound',
            'message': 'Imagem informada não existe.'
    }
    #error_message = {'error': 'Requisição falhou! Imagem não localizada no bucket.'}
    return create_http_response(500, error_message)
