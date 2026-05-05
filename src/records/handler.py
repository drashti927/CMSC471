import os
import json
import boto3

dynamodb = boto3.client('dynamodb')
TABLE = os.environ['RECORDS_TABLE_NAME']

def handler(event, context):
    method = event.get("httpMethod")

    if method == "GET":
        resp = dynamodb.scan(TableName=TABLE)
        items = [
            {
                "recordId": i["recordId"]["S"],
                "filename": i["filename"]["S"],
                "status": i["status"]["S"],
                "timestamp": i["timestamp"]["S"]
            }
            for i in resp.get("Items", [])
        ]
        return {"statusCode": 200, "body": json.dumps(items)}

    if method == "DELETE":
        record_id = event.get("pathParameters", {}).get("id")
        if not record_id:
            return {"statusCode": 400, "body": json.dumps({"error": "id required"})}

        dynamodb.delete_item(
            TableName=TABLE,
            Key={"recordId": {"S": record_id}}
        )
        return {"statusCode": 200, "body": json.dumps({"deleted": record_id})}

    return {"statusCode": 405, "body": "Method not allowed"}
