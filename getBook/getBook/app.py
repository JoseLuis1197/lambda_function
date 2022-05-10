import json
from testDatabase import TestDatabase

# import requests


def lambda_handler(event, context):

    ppBookId = event["pathParameters"]["book-id"]

    book = TestDatabase()

    args = [ppBookId]

    bodyResponse = {}

    statusCode, bodyResponse = book.getBook(args)

    return {
        "statusCode": statusCode,
        "body": bodyResponse
    }
