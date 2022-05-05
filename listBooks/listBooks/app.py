from testDatabase import TestDatabase
import json

def lambda_handler(event, context):

    ##Getting the query params from the event
    if 'queryStringParameters' in event and 'name' in event['queryStringParameters']:
        qpName = event['queryStringParameters']['name']
    else:
        qpName = "None"
    
    if 'queryStringParameters' in event and 'autorName' in event['queryStringParameters']:
        qpAutor = event['queryStringParameters']['autorName']
    else:
        qpAutor = "None"

    ##args = [qpName,qpAutor]

    ##test = TestDatabase()

    ##statusCode, body = test.listBooks(args)

    return {
        ##"statusCode": statusCode,
        "statusCode": 200,
        "body": json.dumps({"data":qpName,"data1":qpAutor})
    }
