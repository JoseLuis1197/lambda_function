from helpers.validation import Validation

def lambda_handler(event, context):

    val = Validation()
    val.validate(event)

    return {
        "statusCode": val.statusCode,
        "body": val.responseBody
    }
