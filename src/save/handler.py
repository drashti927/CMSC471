import os
import json
import boto3
from datetime import datetime, timezone

dynamodb = boto3.client('dynamodb')
TABLE = os.environ['RECORDS_TABLE_NAME']

def handler(event, context):
    record_id = event.get("jobId")
    key = event.get("key")
    text = event.get("text", "")
    timestamp = datetime.now(timezone.utc).isoformat()

    dynamodb.put_item(
        TableName=TABLE,
        Item={
            "recordId": {"S": record_id},
            "filename": {"S": key},
            "status": {"S": "Success"},
            "text": {"S": text},
            "timestamp": {"S": timestamp}
        }
    )

    return {
        "recordId": record_id,
        "filename": key,
        "status": "Success",
        "timestamp": timestamp
    }
