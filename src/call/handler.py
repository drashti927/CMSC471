import json

def handler(event, context):
    return {
        "jobId": event.get("jobId"),
        "key": event.get("key"),
        "text": "Sample extracted text"
    }
