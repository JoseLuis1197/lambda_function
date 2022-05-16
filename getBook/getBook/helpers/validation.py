from testDatabase import TestDatabase
import json

class Validation():

  def __init__(self) -> None:
      pass
      self.statusCode = 0
      self.responseBody = ""
      
  def validate(self,bookId):

    q = TestDatabase()

    args = []
    args.append(bookId)

    resultBook,resultImages = q.getBook(args)

    if len(resultBook) == 0:
      self.statusCode = 200
      self.responseBody = json.dumps({'data':{}})
      return Validation

    bookDict = {}

    ## Creating a dictionary for book information
    for r in resultBook:
      bookDict = {
                  'id': r[0],
                  'name': r[1],
                  'description': r[2],
                  'stars': r[3],
                  'language': r[4],
                  'releaseYear': r[5],
                  'isbn': r[6],
                  'stock': r[7],
                  'pagesNumber': r[8],
                  'priceInformation': {
                    'amount': float(r[9]),
                    'currency': 'USD'
                  },
                  'autor': {
                    'id': r[10],
                    'fullName': r[11],
                    'country': r[12],
                    'birthDate': r[13]
                  },
                  'editor':{
                    'id': r[14],
                    'name': r[15]
                  }
                }

    if len(resultImages) == 0:
      self.statusCode = 200
      self.responseBody = json.dumps({'data':bookDict})
      return Validation

    images = []
    
    for r in resultImages:
      image = {
        'id':r[0],
        'name':r[1],
        'address':r[2]
      }

      images.append(image)

    bookDict["images"] = images

    self.statusCode = 200
    self.responseBody = json.dumps({'data':bookDict})
    return Validation