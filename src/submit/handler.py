import os
import json
import boto3
import uuid

sf = boto3.client('stepfunctions')
dynamodb = boto3.client('dynamodb')

STATE_MACHINE_ARN = os.environ['STATE_MACHINE_ARN']
JOBS_TABLE_NAME = os.environ['JOBS_TABLE_NAME']

def handler(event, context):
    body = json.loads(event.get('body', '{}'))
    key = body.get('key')

    if not key:
        return {"statusCode": 400, "body": json.dumps({"error": "key required"})}

    job_id = str(uuid.uuid4())

    sf.start_execution(
        stateMachineArn=STATE_MACHINE_ARN,
        input=json.dumps({"jobId": job_id, "key": key})
    )

    dynamodb.put_item(
        TableName=JOBS_TABLE_NAME,
        Item={
            "jobId": {"S": job_id},
            "status": {"S": "STARTED"},
            "key": {"S": key}
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"jobId": job_id, "status": "STARTED"})
    }
