import json
import boto3

def lambda_handler(event, context):

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')
    
    # Create the DynamoDB table.
    table = dynamodb.Table('CrcDb')

    table.put_item(
   Item={
        'count': '5',
    }
)

    
    # Print out some data about the table.
    print(table.item_count)