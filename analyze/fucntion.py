import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    rekognition = boto3.client('rekognition')
    cloudwatch = boto3.client('cloudwatch')

    try:
        # Processar cada registro/evento recebido
        for record in event['Records']:
            bucket_name = record['s3']['bucket']['name']
            object_key = record['s3']['object']['key']
            image_id = object_key.rsplit('.', 1)[0]  # Extrair o ID da imagem sem a extensão

            # Realizar a análise da imagem usando o Rekognition
            rekognition_params = {
                'Image': {
                    'S3Object': {
                        'Bucket': kelly-serverless-sprint8-2,
                        'Name': object_key
                    }
                },
                # Especificar os recursos de análise necessários (exemplo: detecção de rostos)
                'Attributes': ['ALL']
            }
            rekognition_result = rekognition.detect_faces(**rekognition_params)

            # Enviar métricas para o CloudWatch
            metrics_params = {
                'Namespace': 'ImageAnalysis',
                'MetricData': [
                    {
                        'MetricName': 'FaceCount',
                        'Dimensions': [
                            {
                                'Name': 'ImageId',
                                'Value': image_id
                            }
                        ],
                        'Unit': 'Count',
                        'Value': len(rekognition_result['FaceDetails'])
                    }
                ]
            }
            cloudwatch.put_metric_data(**metrics_params)

        return {
            'statusCode': 200,
            'body': 'Images analyzed successfully.'
        }
    except Exception as e:
        print('Error:', e)
        return {
            'statusCode': 500,
            'body': 'An error occurred while analyzing the images.'
        }
