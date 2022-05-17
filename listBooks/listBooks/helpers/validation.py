from asyncio.windows_events import NULL
from testDatabase import TestDatabase
import json

class Validation():

  def __init__(self) -> None:
    statusCode = 0
    responseBody = ""

  def validate(self,queryP):

    ##Getting the query params from the event

    qpName = ""
    qpAutor = ""
    qpScore = 0
    qpLimit = 20
    qpOffset = 0

    if 'queryStringParameters' in queryP:
        if 'name' in queryP['queryStringParameters']:
            qpName = queryP['queryStringParameters']['name']

        if 'autorName' in queryP['queryStringParameters']:
            qpAutor = queryP['queryStringParameters']['autorName']

        if 'pageSize' in queryP['queryStringParameters']:
            qpLimit = queryP['queryStringParameters']['pageSize']

        if 'pageOffset' in queryP['queryStringParameters']:
            qpOffset = queryP['queryStringParameters']['pageOffset']
    
    args = [qpName,qpAutor,qpScore,qpLimit,qpOffset]

    q = TestDatabase()
    resultSet = q.listBooks(args)

    bookDict = []    

    ## Creating a dictionary
    for row in resultSet:

      if len(bookDict) != 0:
        bookDict[len(bookDict)-1]["id"] = row[0]
        next       

      o = {
            'id':row[0],
            'name':row[1],
            'description':row[2],
            'stars':row[3],
            'language':row[4],
            'releaseYear':row[5],
            'isbn':row[6],
            'stock':row[7],
            'pagesNumber':row[8],
            'priceInformation': {
              'amount':float(row[9]),
              'currency': 'PEN'
            },
            'autor':{
              'id': row[10],
              'name': row[11],
              'country': row[12]
            }
          }

      bookDict.append(o)    

      if row[13] != NULL or row[13] == "":
        images = [
          {
            "id": row[13],
            "name": row[15],
            "address": row[16]
          }
        ]
        
        bookDict["images"] = images     


    self.statusCode = 200
    self.responseBody = json.dumps({'data':bookDict})
    return Validation