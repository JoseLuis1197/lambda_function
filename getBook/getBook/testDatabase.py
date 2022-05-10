from unittest import result
from getDatabase import ConnectionDatabase
import json
from datetime import datetime

class TestDatabase:

  spNameGetBook = 'spGetBook'

  def __init__(self) -> None:
    pass
  
  def getBook(self,args):
    
    con = ConnectionDatabase()    

    resultSet = con.consumeStoreProcedure(self.spNameGetBook,args)   

    bookDict = {}

    if len(resultSet) == 0:
      return 200,json.dumps({'data':{}})


    ## Creating a dictionary
    for r in resultSet:
      bookDict = {
                  'id': r[0],
                  'name': r[1],
                  'description': r[2],
                  'stars': r[3],
                  'images': [
                    {
                      'address': r[4]
                    }
                  ],
                  'language': r[5],
                  'releaseYear': r[6],
                  'isbn': r[7],
                  'stock': r[8],
                  'pagesNumber': r[9],
                  'priceInformation': {
                    'amount': float(r[10]),
                    'currency': 'USD'
                  },
                  'autor': {
                    'id': r[11],
                    'fullName': r[12],
                    'country': r[13],
                    'birthDate': r[14]
                  },
                  'editor':{
                    'id': r[15],
                    'name': r[16]
                  }
                }

      return 200,json.dumps({'data':bookDict})