import boto3
import json

def v2_vision(event, context):
    
    request_body = json.loads(event['body'])
    
    bucket = request_body['bucket']
    imageName = request_body['imageName']
    
    url_to_image = f"https://{bucket}/{imageName}"
    
    # Conectar-se ao AWS Rekognition e seleciona o serviço de detecção de faces
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
    
    # Verificar se há faces detectadas na imagem
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
        # Extrair as informações das faces detectadas
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
            'created_image': '02-02-2023 17:00:00',
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

