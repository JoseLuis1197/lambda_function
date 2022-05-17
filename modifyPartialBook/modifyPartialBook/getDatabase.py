from multiprocessing import connection
import mysql.connector
from mysql.connector import Error

import json

class ConnectionDatabase:

  def __init__(self):
    pass

  def consumeStoreProcedure(self,spName,args):    
  
    try:      
              
      with open('./config.json') as f:
        config = json.load(f)

      connection = mysql.connector.connect(host=config['databaseInfo']['endpoint'],
                                        database=config['databaseInfo']['databaseName'],
                                        user=config['databaseInfo']['user'],
                                        password=config['databaseInfo']['password']) 
      cursor = connection.cursor()
      cursor.callproc(spName, args)   

      for result in cursor.stored_results():
        rfetch = result.fetchall()                 
        
      return rfetch

    except mysql.connector.Error as error:
      print("Failed to execute stored procedure: {}".format(error))
    finally:
      if (connection.is_connected()):
        cursor.close()
        connection.close()
  
  def consumeCreationStoreProcedure(self,spName,args):    
  
    try:      

      with open('./config.json') as f:
        config = json.load(f)

      connection = mysql.connector.connect(host=config['databaseInfo']['endpoint'],
                                        database=config['databaseInfo']['databaseName'],
                                        user=config['databaseInfo']['user'],
                                        password=config['databaseInfo']['password'])

      cursor = connection.cursor()
      result_args = cursor.callproc(spName, args)         
                         
      return result_args[-1]

    except mysql.connector.Error as error:
      print("Failed to execute stored procedure: {}".format(error))
    finally:
      if (connection.is_connected()):
        cursor.close()
        connection.close()
        ##print("MySQL connection is closed")

  def insertManyIntoOrderDetail(self,items):
    try:     

      with open('./config.json') as f:
        config = json.load(f)

      connection = mysql.connector.connect(host=config['databaseInfo']['endpoint'],
                                        database=config['databaseInfo']['databaseName'],
                                        user=config['databaseInfo']['user'],
                                        password=config['databaseInfo']['password'])

      cursor = connection.cursor()
      stmt = "insert into tblOrdersDetail(iId,idBook,fBookPrice,iBookQuantity,fBookTotalPrice,iIdOrder) values (null,%s,%s,%s,%s,%s)"
      cursor.executemany(stmt,items)    
      connection.commit()

    except mysql.connector.Error as error:
      print("Failed to execute stored procedure: {}".format(error))
    finally:
      if (connection.is_connected()):
        cursor.close()
        connection.close()
        ##print("MySQL connection is closed")