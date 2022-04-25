from testDatabase import TestDatabase


def lambda_handler(event, context):
    test = TestDatabase()

    return {
        "statusCode": 200,
        "body": test.listBooks(),
    }

