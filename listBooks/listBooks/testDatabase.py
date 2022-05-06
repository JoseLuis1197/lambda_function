from getDatabase import ConnectionDatabase
import json
from datetime import datetime

class TestDatabase:

  spNameGetOrder = 'spGetOrderDetail'
  spNameCreateBook = 'spCreateBook'
  spNameCreateAutor = 'spCreateAutor'
  spNameUpdateAutor = 'spUpdateAutor'
  spNameCreateCustomerAddress = 'spCreateCustomerAddress'
  spNameUpdateCustomerAddress = 'spUpdateCustomerAddress'
  spNameListCustomerAddresses = 'spListCustomerAddresses'
  spNameGetCartDetail = 'spGetCart'
  spNameCreateOrder = 'spCreateOrder'
  spNameCreateOrderDetail = 'spAddItemsToOrder'
  spNameListBooks = 'spListBooks'
  spNameGetBook = 'spGetBook'

  def __init__(self) -> None:
    pass
  

  def getOrder(self,orderId):

    args = [int(orderId)]   

    con = ConnectionDatabase()
    resultSet = con.consumeStoreProcedure(self.spNameGetOrder,args)    

    for row in resultSet._rows:
      print('Id:', row[0])
      print('Id adress: ',row[1])
      print('Ubicacion: ', row[2])
      print('Distrito: ', row[3])
      print('Provincia: ', row[4])
      print('Departamento: ', row[5])
      print('Referencia: ', row[6])
      print('Latitud: ', row[7])
      print('Longitud: ', row[8])
      print('Google place id: ', row[9])
      print('Tipo de pago: ', row[11])
      print('Id transacción: ', row[12])
      print('Costo de envío: ', row[13])
      print('Costo de la orden: ', row[14])
      print('Entregado: ', row[15])
      print('Fecha de envío: ', row[16])
      print('Fecha de creación: ', row[17])
      print('Id libro: ', row[19])
      print('Nombre del libro: ', row[20])
      print('Costo del libro: ', row[22])
      print('Cantidad de libro: ', row[23])
      print('Costo total del libro: ', row[24])
      print('\n')  

  def createBook(self):    

    args = []
    args.append('No me esperen en abril otra vez II')
    args.append('Es el primer libro que leí')
    args.append(4)
    args.append('jpg')
    args.append('Espanol')
    args.append(1990)
    args.append('39IFJ3O3JR')
    args.append(500)
    args.append(700)
    args.append(60)
    args.append(1)
    args.append(1)

    con = ConnectionDatabase()    
    resultSet = con.consumeStoreProcedure(self.spNameCreateBook,args)
    
    for row in resultSet._rows:
      valor = row[0]
    
    if isinstance(valor,int):
      print('El valor creado es:',valor)
    else:
      print('Alguno de los valores enviados, ya existe.')    

  def createAutor(self):
    args = ['Maria Arguedas','1874-11-12','Perú']       

    con = ConnectionDatabase()
    resultSet = con.consumeStoreProcedure(self.spNameCreateAutor,args)

    for row in resultSet._rows:
      valor = row[0]
    
    if isinstance(valor,int):
      print('El valor creado es:',valor)
    else:
      print('Alguno de los valores enviados, ya existe.')      

  def updateAutor(self,autorId):
    args=[autorId,'Mario Vargas Llosa','1928-03-02','Perú']    

    con = ConnectionDatabase()
    con.consumeStoreProcedure(self.spNameUpdateAutor,args)

    print('Se actualizó correctamente el registro.')

  def createCustomerAddress(self,customerId):
    args=[]
    args.append(customerId)
    args.append('Calle Chavin 419')
    args.append('Santa Anita')
    args.append('Lima')
    args.append('Lima')
    args.append('Al lado de otro edificio')
    args.append(0)
    args.append(0)
    args.append('U3EU229U')    

    con = ConnectionDatabase()
    con.consumeStoreProcedure(self.spNamecreateCustomerAddress,args)

    print('Se agregó correctamente la dirección.')

  def updateCustomerAddress(self,customerId):
    args=[]
    args.append(customerId)
    args.append('Avenida de la republica')
    args.append('San Isidro')
    args.append('Lima')
    args.append('Lima')
    args.append('Al lado de otro edificio II')
    args.append(0)
    args.append(0)
    args.append('I3I0DI')
    args.append(0)    

    con = ConnectionDatabase()
    con.consumeStoreProcedure(self.spNameUpdateCustomerAddress,args)

    print('Se actualizó correctamente el registro')

  def listCustomerAddresses(self,customerId):

    args=[]
    args.append(customerId)       

    con = ConnectionDatabase()
    resultSet = con.consumeStoreProcedure(self.spNameListCustomerAddresses,args)    

    print('El cliente tiene {} direcciones.'.format(resultSet._rowcount))
  
  def getCartDetail(self,customerEmail):
    args = [customerEmail]
    con = ConnectionDatabase()
    resultSet = con.consumeStoreProcedure(self.spNameGetCartDetail,args)       

    return resultSet

  def createOrder(self,args):
    con = ConnectionDatabase()
    resultSet = con.consumeCreationStoreProcedure(self.spNameCreateOrder,args)   
    
    return resultSet
  
  def createOrderDetail(self,args):    

    con = ConnectionDatabase()
    
    resultSet = con.consumeCreationStoreProcedure(self.spNameCreateOrderDetail,args)       

    return resultSet
  
  def insertOrderDetail(self,args):
    con = ConnectionDatabase()
    
    con.insertManyIntoOrderDetail(args)

    return 'OK'
  
  def listBooks(self,args):
    
    con = ConnectionDatabase()    

    resultSet = con.consumeStoreProcedure(self.spNameListBooks,args)

    bookDict = []    

    ## Creating a dictionary
    for row in resultSet:
      o = {
            'id':row[0],
            'name':row[1],
            'description':row[2],
            'stars':row[3],
            'images':[
              {
                'address':row[4]
              }
            ],
            'language':row[5],
            'releaseYear':row[6],
            'isbn':row[7],
            'stock':row[8],
            'pagesNumber':row[9],
            'priceInformation': {
              'amount':float(row[10]),
              'currency': 'PEN'
            }
          }

      bookDict.append(o)    

    return 200,json.dumps({'data':bookDict})

  def getBook(self,args):
    
    con = ConnectionDatabase()    

    resultSet = con.consumeStoreProcedure(self.spNameGetBook,args)

    if resultSet[0] == 'ERROR':
      return 400,json.dumps({'alias':'bookNotFound','message':resultSet[1]})    

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