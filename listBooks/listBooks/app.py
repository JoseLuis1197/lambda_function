from testDatabase import TestDatabase

def lambda_handler(event, context):

    ##Getting the query params from the event

    qpName = ""
    qpAutor = ""
    qpScore = ""
    qpLimit = 0
    qpOffset = 0

    if 'queryStringParameters' in event:
        if 'name' in event['queryStringParameters']:
            qpName = event['queryStringParameters']['name']

        if 'autorName' in event['queryStringParameters']:
            qpAutor = event['queryStringParameters']['autorName']
    
    args = [qpName,qpAutor,qpScore,qpLimit,qpOffset]

    books = TestDatabase()

    body = {}

    statusCode, body = books.listBooks(args)

    return {
        "statusCode": statusCode,
        "body": body
    }
