from testDatabase import TestDatabase
import json

def lambda_handler(event, context):

    ##Getting the query params from the event
    qpName = event['queryStringParameters']['name']
    qpAutor = event['queryStringParameters']['autorName']

    ##args = [qpName,qpAutor]

    ##test = TestDatabase()

    ##statusCode, body = test.listBooks(args)

    return {
        ##"statusCode": statusCode,
        "statusCode": 200,
        "body": json.dumps({"data":qpName})
    }
