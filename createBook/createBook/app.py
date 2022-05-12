import json
from testDatabase import TestDatabase

def lambda_handler(event, context):

    ## Inicializar los datos de la creación del libro

    args = []

    ##Adding name
    if event["body"]["name"]:
        args.append = event["body"]["name"]

    #Adding description
    if event["body"]["description"]:
        args.append = event["body"]["description"]
    
    args.append = 0

    args.append = ""

    #Adding language
    if event["body"]["language"]:
        args.append = event["body"]["language"]

    #Adding release year
    if event["body"]["releaseYear"]:
        args.append = event["body"]["releaseYear"]

    #Adding isbn code
    if event["body"]["isbn"]:
        args.append = event["body"]["isbn"]

    args.append = 0    

    #Adding pages number
    if event["body"]["pagesNumber"]:
        args.append = event["body"]["pagesNumber"]

    #Adding book price
    if event["body"]["price"]["amount"]:
        args.append = event["body"]["amount"]
    #Adding editor id
    if event["body"]["editor"]["id"]:
        args.append = event["body"]["editor"]["id"]

    #Adding autor id
    if event["body"]["autor"]["id"]:
        args.append = event["body"]["autor"]["id"]

    book = TestDatabase()
    bodyResponse = {}
    statusCode, bodyResponse = book.createBook(args)

    return {
        "statusCode": statusCode,
        "body": bodyResponse
    }
