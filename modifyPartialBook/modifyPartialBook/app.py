import json


def lambda_handler(event, context):

    bookId = event["pathParameters"]["book-id"]

    print(bookId)

    return {
        "statusCode": 204,
        "body": json.dumps({"message": "hello world"})
    }
