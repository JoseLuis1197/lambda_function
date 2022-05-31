from testDatabase import TestDatabase
import json

class Validation():

  def __init__(self) -> None:
    statusCode = 0
    responseBody = ""

  def validate(self,bookId,params):    

    args = []
    args.append(int(bookId))

    #Se validan los campos requeridos para asociar la imagen a la BD
    if "address" in params:
      args.append(params["address"])
    else:
      self.statusCode = 400
      self.responseBody = json.dumps({"alias":"requiredFielMissing","message":"El campo address no ha sido informado."})
    
    if "isPrincipal" in params:
      args.append(params["isPrincipal"])
    else:
      self.statusCode = 400
      self.responseBody = json.dumps({"alias":"requiredFielMissing","message":"El campo isPrincipal no ha sido informado."})      
    
    q = TestDatabase()
    resultSet = q.createBook(args)

    ## Creating a dictionary
    for row in resultSet:
      imageId = int(row[0])
      break
    
    self.statusCode = 201
    self.responseBody = json.dumps({'data':imageId})
    return Validation