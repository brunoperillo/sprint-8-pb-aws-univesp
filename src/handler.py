from .utils import create_http_response

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = create_http_response(200, body)

    return response

def v1_description(event, context):
    body = {
        "message": "VISION api version 1."
    }

    response = create_http_response(200, body)

    return response

def v2_description(event, context):
    body = {
        "message": "VISION api version 2."
    }

    response = create_http_response(200, body)

    return response

