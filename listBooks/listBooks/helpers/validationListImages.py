from testDatabase import TestDatabase
import json

class Validation():

  def __init__(self) -> None:
    statusCode = 0
    responseBody = ""

  def validate(self,bookId):

    args = [bookId]

    q = TestDatabase()
    resultSet = q.listBookImages(args)

    bookDict = []    

    ## Creating a dictionary
    for row in resultSet:        
      o = {
            'id':int(row[0]),
            'name':row[1],
            'address':row[2],
            'isPrincipal':bool(row[3]),  
						'imageType': row[4]          
          }     
        
      bookDict.append(o)   
    
    self.statusCode = 200
    self.responseBody = json.dumps({'data':bookDict})
    return Validation