import boto3
import json
from .utils import get_image_creation_date


def v2_vision(event, context):
    
    request_body = json.loads(event['body'])
    
    bucket = request_body['bucket']
    imageName = request_body['imageName']
    
    url_to_image = f"https://{bucket}/{imageName}"
    
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

        #'created_image': '02-02-2023 17:00:00',

        result = {
            'url_to_image': url_to_image,
            'created_image': get_image_creation_date(bucket, imageName),  
            'faces': faces
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

'''
def get_image_creation_date(bucket, imageName):
    """
    Obtém a data de criação de uma imagem no bucket do Amazon S3.

    Args:
        bucket (str): Nome do bucket do Amazon S3.
        imageName (str): Nome da imagem.

    Returns:
        str: Data de criação da imagem no formato '%d-%m-%Y %H:%M:%S'.
    """
    s3 = boto3.client('s3')
    
    response = s3.head_object(Bucket=bucket, Key=imageName)
    creation_date = response['LastModified'].strftime('%d-%m-%Y %H:%M:%S')
    
    return creation_date
'''
