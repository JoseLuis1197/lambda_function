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

    resultBook,resultImages = con.consumeStoreProcedure(self.spNameGetBook,args)   

    return resultBook,resultImages