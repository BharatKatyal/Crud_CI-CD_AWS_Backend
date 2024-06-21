import boto3
import os
import json
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['ITEMS_TABLE_NAME'])

def handler(event, context):
    try:
        body = json.loads(event['body'])
        item_id = str(uuid.uuid4())
        item = {
            "id": item_id,
            **body
        }
        table.put_item(Item=item)
        return {
            "statusCode": 201,
            "body": json.dumps(item)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error!": str(e)})
        }
