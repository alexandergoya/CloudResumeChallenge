import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')
    
    # Create the DynamoDB table.
    table = dynamodb.Table('CrcDb')

    response = table.get_item(
        Key={
            'count': '2'
        }
    )
    #print(response['Item'])
    # item = response[Item.NewValue]
    # if item == None:
    #     item = 0
    # item += 1
    #print(item)
    response = table.query(
        KeyConditionExpression=Key('count').eq('2')
    )
    # Extract results
    items = response['Items']
    for item in items:
        NewValue = 1 + item['NewValue']
        print('----------')
        print(str(NewValue))
        print('--------------')
    
    table.update_item(
        Key={
            'count': '2'
        },
        UpdateExpression='SET NewValue = :val1',
        ExpressionAttributeValues={
            ':val1': NewValue
        }
    )