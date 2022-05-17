import json
from helpers.validation import Validation


def lambda_handler(event, context):

    bookId = event["pathParameters"]["book-id"]
    val = Validation()
    val.updateBook(bookId,json.loads(event['body']))

    return {
        "statusCode": val.statusCode,
        "body": val.bodyResponse
    }