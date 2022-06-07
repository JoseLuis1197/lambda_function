from getDatabase import ConnectionDatabase
import json

class TestDatabase:

  spNameCreateBook = 'spCreateBook'

  def __init__(self) -> None:
    pass
  
  def createBook(self,args):

    con = ConnectionDatabase()    
    resultSet = con.consumeStoreProcedure(self.spNameCreateBook,args)
  
    for r in resultSet:
      if r[0] == "OK":
        bookId = r[1]
        return 201, json.dumps({"data":{"id":bookId}})
      else:
        return 400, json.dumps({"alias":"autorInvalid","message":"Autor or editor id is invalid."})

    return 500, json.dumps({"alias":"internalError"})