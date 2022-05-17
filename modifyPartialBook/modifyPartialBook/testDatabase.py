from unittest import result
from getDatabase import ConnectionDatabase
import json
from datetime import datetime

class TestDatabase:

  spNameGetBook = 'spGetBook'
  spNameModifyBook = 'spModifyPartialBook'


  def __init__(self) -> None:
    pass
  
  def getBook(self,args):
    
    con = ConnectionDatabase()    

    resultSet = con.consumeStoreProcedure(self.spNameGetBook,args)   

    return resultSet

  def modifyBook(self,args):

    con = ConnectionDatabase()

    resultSet = con.consumeStoreProcedure(self.spNameModifyBook,args)   

    return resultSet
    