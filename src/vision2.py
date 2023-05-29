import boto3
import botocore.exceptions
import json
from .utils import get_image_creation_date, create_http_response

def v2_vision(event, context):
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
    
    # Conecta-se ao AWS Rekognition e seleciona o serviço de detecção de faces
    rekognition = boto3.client('rekognition')
    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': imageName
            }
        },
        Attributes=['ALL']  # Retorna todos os atributos das faces detectadas
    )
    
    # Verifica se foi detectada alguma face na imagem. Em caso negativo, responde à requisição com o formato especificado
    if len(response['FaceDetails']) == 0:
        result = {
            'url_to_image': url_to_image,
            'created_image': '02-02-2023 17:00:00',
            'faces': [
                {
                    'position': {
                        'Height': 'Null',
                        'Left': 'Null',
                        'Top': 'Null',
                        'Width': 'Null'
                    },
                    'classified_emotion': 'Null',
                    'classified_emotion_confidence': 'Null'
                }
            ]
        }
    else:
        # Caso haja face na imagem, extrai as informações da(s) face(s) detectada(s)
        faces = []
        for face in response['FaceDetails']:
            face_info = {
                'position': {
                    'Height': face['BoundingBox']['Height'],
                    'Left': face['BoundingBox']['Left'],
                    'Top': face['BoundingBox']['Top'],
                    'Width': face['BoundingBox']['Width']
                },
                'classified_emotion': face['Emotions'][0]['Type'],
                'classified_emotion_confidence': face['Emotions'][0]['Confidence']
            }
            faces.append(face_info)

        result = {
            'url_to_image': url_to_image,
            'created_image': get_image_creation_date(bucket, imageName),
            'faces': faces
        }

    # Imprime o resultado nos logs do CloudWatch
    print(result)

    response = create_http_response(200, result)
    return response

