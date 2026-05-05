import os
import json
import boto3

dynamodb = boto3.client('dynamodb')
TABLE = os.environ['JOBS_TABLE_NAME']

def handler(event, context):
    job_id = event.get("jobId")
    if not job_id:
        return {"error": "jobId required"}

    resp = dynamodb.get_item(
        TableName=TABLE,
        Key={"jobId": {"S": job_id}}
    )

    item = resp.get("Item")
    if not item:
        return {"jobId": job_id, "status": "UNKNOWN"}

    return {
        "jobId": job_id,
        "status": item["status"]["S"]
    }
