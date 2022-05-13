import json
from testDatabase import TestDatabase
from helpers.validation import validation

def lambda_handler(event, context):

    ## Inicializar los datos de la creación del libro

    bodyRequest = json.loads(event['body'])
    val = validation()
    val.validateCreationBookRequest(bodyRequest)

    if val.status == "OK":
        book = TestDatabase()
        bodyResponse = {}
        statusCode, bodyResponse = book.createBook(val.validationResponse)

    else:
        statusCode = 400
        bodyResponse = "Mal"

    return {
        "statusCode": statusCode,
        "body": bodyResponse
    }
