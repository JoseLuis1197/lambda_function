from testDatabase import TestDatabase

def lambda_handler(event, context):

    ##Getting the query params from the event

    qpName = ""
    qpAutor = ""
    qpScore = 0
    qpLimit = 20
    qpOffset = 0

    if 'queryStringParameters' in event:
        if 'name' in event['queryStringParameters']:
            qpName = event['queryStringParameters']['name']

        if 'autorName' in event['queryStringParameters']:
            qpAutor = event['queryStringParameters']['autorName']

        if 'pageSize' in event['queryStringParameters']:
            qpLimit = event['queryStringParameters']['pageSize']

        if 'pageOffset' in event['queryStringParameters']:
            qpLimit = event['queryStringParameters']['pageOffset']
    
    args = [qpName,qpAutor,qpScore,qpLimit,qpOffset]

    books = TestDatabase()

    body = {}

    statusCode, body = books.listBooks(args)

    return {
        "statusCode": statusCode,
        "body": body
    }
