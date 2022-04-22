from testDatabase import TestDatabase

# import requests


def lambda_handler(event, context):

    test = TestDatabase()


    return {
        "statusCode": 200,
        "body": test.listBooks(),
    }
