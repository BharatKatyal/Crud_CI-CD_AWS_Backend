import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['ITEMS_TABLE_NAME'])

def handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        response = table.get_item(Key={'id': item_id})
        item = response.get('Item')
        if not item:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Item not found!"})
            }
        return {
            "statusCode": 200,
            "body": json.dumps(item)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
