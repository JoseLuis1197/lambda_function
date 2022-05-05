from testDatabase import TestDatabase
import json

def lambda_handler(event, context):


    ##Getting the query params from the event
    qpName = event['queryStringParameters']['Name']
    qpAutor = event['queryStringParameters']['AutorName']

    args = [qpName,qpAutor]

    test = TestDatabase()

    statusCode, body = test.listBooks(args)

    return {
        "statusCode": statusCode,
        "body": json.dumps({"data":qpName})
    }
