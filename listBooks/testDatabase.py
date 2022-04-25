from getDatabase import ConnectionDatabase
import json
from datetime import datetime

class TestDatabase:

  spNameListBooks = "spListBooks"

  def __init__(self) -> None:
      pass
  
  def listBooks(self):

    args = []
    bookDict = []
    print("Hora de abrir conexión: "+str(datetime.now()))
    con = ConnectionDatabase()
    print("Ir a sacar data del sp: "+str(datetime.now()))

    resultSet = con.consumeStoreProcedure(self.spNameListBooks,args)

    print("Hora de fin para sacar data sp: "+str(datetime.now()))
    print("Hora de inicio del diccionario: "+str(datetime.now()))

    ## Creating a dictionary
    for row in resultSet:
      o = {
            "id":row[0],
            "name":row[1],
            "description":row[2],
            "stars":row[3],
            "images":[
              {
                "address":row[4]
              }
            ],
            "language":row[5],
            "releaseYear":row[6],
            "isbn":row[7],
            "stock":row[8],
            "pagesNumber":row[9],
            "priceInformation": {
              "amount":row[10],
              "currency": "PEN"
            }
          }

      bookDict.append(o)

    print("Hora de fin del diccionario: " + str(datetime.now()))

    return json.dumps({"data":bookDict})