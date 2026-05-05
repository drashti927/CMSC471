import boto3
import os

s3 = boto3.client('s3')

def proxy_handler(event, context):
    bucket = os.environ['BUCKET_NAME']
    
    response = s3.get_object(Bucket=bucket, Key='index.html')
    html = response['Body'].read().decode('utf-8')

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html
    }
