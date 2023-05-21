import json
import boto3
from datetime import datetime, date

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
    
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)
    
def v1Label(event, context):
    # Extract bucket name and image name from the POST request body
    bucket_name = event['bucket']
    image_name = event['imageName']
    
    #S3 connection
    s3_client = boto3.client('s3')
    
    # Create an Amazon Rekognition client
    rekognition = boto3.client("rekognition")

    # Call Amazon Rekognition to detect labels in the image
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': image_name}},
        MaxLabels=5  # Change this value for more or fewer labels
    )

    # Extract the detected labels from the response
    labels = [{'confidence': label['Confidence'], 'label': label['Name']} for label in response["Labels"]]
    
    
    # Get the metadata of the image object
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=image_name)
        image_url = f"https://{bucket_name}.s3.amazonaws.com/{image_name}"
        creation_time = response['LastModified']
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
        
    # Convert the datetime object to a string in ISO 8601 format
    creation_time_str = creation_time.isoformat()

    # Create a dictionary representing the JSON body
    response_body = {
        "url_to_image": image_url,
        "created_image": creation_time,
        "labels": labels
    }
    
    print(response_body)

    # Convert the dictionary to a JSON string using the custom encoder
    response_json = json.dumps(response_body, cls=CustomEncoder)

    print(response_json)
    
    # Return the JSON string as the response body of the Lambda function
    return {
        'statusCode': 200,
        'body': response_json
    }
'''
def v1Label(event, context):
    # Extract bucket name and image name from the POST request body
    bucket_name = event['bucket']
    image_name = event['imageName']

    # Create an Amazon Rekognition client
    rekognition = boto3.client('rekognition')

    # Call Amazon Rekognition to detect labels in the image
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': image_name}},
        MaxLabels=10  # Change this value if you want more or fewer labels
    )

    labels = []
    # Extract the detected labels from the response
    print('Detected labels for image: ' + image_name)
    print()
    for label in response['Labels']:
        print ("Confidence: " + str(label['Confidence']))
        print ("Label: " + label['Name'])
        print('---------------|')
    # Return the labels as the response of the Lambda function
    
    
    return {"statusCode": 200, "body": json.dumps(body)}'''


def v2Emotion():
    body = {
        "message": "Emotion API gateway is working"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response