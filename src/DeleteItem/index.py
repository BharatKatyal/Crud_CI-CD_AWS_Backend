import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['ITEMS_TABLE_NAME'])

def handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        response = table.delete_item(Key={'id': item_id})
        return {
            "statusCode": 204,
            "body": json.dumps({})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
