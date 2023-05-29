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


def v1vision_description(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")

    # reading file from s3 bucket and passing it as bytes
    fileObj = s3.get_object(Bucket="bucket-images-sprint8", Key="10095785.jpg")
    file_content = fileObj["Body"].read()

    # passing bytes data
    response = client.detect_labels(
        Image={"Bytes": file_content}, MaxLabels=3, MinConfidence=70
    )

    labels = [{'confidence': label['Confidence'], 'Name': label['Name']} for label in response["Labels"]]
    
    return labels


def v2_description(event, context):
    body = {
        "message": "VISION api version 2."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2vision_description(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")

    # reading file from s3 bucket and passing it as bytes
    fileObj = s3.get_object(Bucket="bucket-images-sprint8", Key="1images.jpg")
    file_content = fileObj["Body"].read()

    # passing bytes data
    response = client.detect_faces(
        Image={"Bytes": file_content}, Attributes=["ALL"]
    )

    print(response)

    return response