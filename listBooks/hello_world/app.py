from testDatabase import TestDatabase

def lambda_handler(event, context):


    ##Getting the query params from the event
    qpName = event['queryStringParameters']['name']
    qpAutor = event['queryStringParameters']['autor']
    qpOffset = event['queryStringParameters']['offset']
    qpLimit = event['queryStringParameters']['limit']

    args = [qpName,qpAutor,qpOffset,qpLimit]

    test = TestDatabase()

    return {
        "statusCode": 200,
        "body": test.listBooks(args),
    }
