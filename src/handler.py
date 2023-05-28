import json
import boto3

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "VISION api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2_description(event, context):
    body = {
        "message": "VISION api version 2."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

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
    for label in response['Labels']:
        labels.append({
            'Name': label['Name'],
            'Confidence': label['Confidence']
        })
    
    result = {
        'url_to_image': url_to_image,
        'created_image': '02-02-2023 17:00:00',
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

'''
def v2_vision(event, context): 
# https://docs.aws.amazon.com/rekognition/latest/dg/faces-detect-images.html
    
    request_body = json.loads(event['body'])
    
    bucket = request_body['bucket']
    imageName = request_body['imageName']
    
    url_to_image = f"https://{bucket}/{imageName}"
    
    # Conectar-se ao AWS Rekognition
    rekognition = boto3.client('rekognition')

    # Executar a detecção de rostos em imagem
    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': imageName
            }
        }
    )

    faces = []
    for faceDetail in response['FaceDetails']:
        faces.append({
            {
            "position":{
                "Height": faceDetail['BoundingBox']['Height'],
                "Left": faceDetail['BoundingBox']['Left'],
                "Top": faceDetail['BoundingBox']['Top'],
                "Width": faceDetail['BoundingBox']['Width']
            },
            "classified_emotion": faceDetail['Emotions']['Type'],
            "classified_emotion_confidence": faceDetail['Emotions']['Confidence']         
        }

        })
    result = {
        'url_to_image': url_to_image,
        'created_image': '02-02-2023 17:00:00',
        'labels': faces
    }
    print(result)

    response = {
        'statusCode': 200,
        'body': json.dumps(result),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
        
    return response
'''