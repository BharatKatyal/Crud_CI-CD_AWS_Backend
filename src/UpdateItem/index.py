import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['ITEMS_TABLE_NAME'])

def handler(event, context):
    try:
        item_id = event['pathParameters']['id']
        body = json.loads(event['body'])
        update_expression = "set " + ", ".join([f"{k}=:{k}" for k in body.keys()])
        expression_attribute_values = {f":{k}": v for k, v in body.items()}
        
        response = table.update_item(
            Key={'id': item_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="ALL_NEW"
        )
        return {
            "statusCode": 200,
            "body": json.dumps(response['Attributes'])
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
