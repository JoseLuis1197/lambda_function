import json
from testDatabase import TestDatabase
from helpers.validation import validation

def lambda_handler(event, context):

    ## Inicializar los datos de la creación del libro

    val = validation()
    
    val.validateCreationBookRequest(event["body"])

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
