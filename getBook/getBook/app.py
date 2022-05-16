from helpers.validation import Validation

def lambda_handler(event, context):

    ppBookId = event["pathParameters"]["book-id"]
    val = Validation()
    val.validate(ppBookId)

    return {
        "statusCode": val.statusCode,
        "body": val.responseBody
    }
