import json
from helpers.validation import Validation

# import requests


def lambda_handler(event, context):

    bookId = event["pathParameters"]["book-id"]
    bodyRequest = json.loads(event["body"])
    val = Validation()
    val.validateCreationBookImage(bookId,bodyRequest)


    return {
        "statusCode": val.statusCode,
        "body": val.bodyResponse
    }
