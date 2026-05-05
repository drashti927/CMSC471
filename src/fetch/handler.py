import os
import json

def handler(event, context):
    return {
        "jobId": event.get("jobId"),
        "key": event.get("key"),
        "bucket": os.environ["INBOX_BUCKET_NAME"]
    }
