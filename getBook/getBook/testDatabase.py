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

    ## Creating a dictionary
    for r in resultSet:
      bookDict = {
                  'id': r[0],
                  'name': r[1],
                  'description': r[2],
                  'stars': r[3],
                  'image': r[4],
                  'language': r[5],
                  'releaseYear': r[6],
                  'isbn': r[7],
                  'stock': r[8],
                  'pagesNumber': r[9],
                  'priceInformation': {
                    'amount': r[10],
                    'currency': r[11]
                  },
                  'autor': {
                    'id': r[12],
                    'fullName': r[13],
                    'country': r[14]
                  },
                  'editor':{
                    'id': r[15],
                    'name': r[16]
                  }
                }

      return 200,json.dumps({'data':bookDict})