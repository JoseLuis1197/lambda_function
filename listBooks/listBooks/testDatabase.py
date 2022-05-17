from getDatabase import ConnectionDatabase
import json
from datetime import datetime

class TestDatabase:

  spNameListBooks = 'spListBooks'

  def __init__(self) -> None:
    pass
  
  def listBooks(self,args):
    
    con = ConnectionDatabase()   
    resultSet = con.consumeStoreProcedure(self.spNameListBooks,args)
    return resultSet