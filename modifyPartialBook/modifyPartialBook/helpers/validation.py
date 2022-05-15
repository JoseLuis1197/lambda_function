from testDatabase import TestDatabase
import json


class Validation:
  def __init__(self) -> None:
      statusCode = 0
      bodyResponse = ""

  def updateBook(self,bookId,body):

    args = []
    args.append(bookId)

    consult = TestDatabase()

    result = consult.getBook(args)

    if len(result) == 0:
      self.statusCode = 400
      self.bodyResponse = json.dumps({"alias":"bookNotFound","message":"El libro con id {0} no fue encontrado".format(bookId)})
      return Validation
    
    #consumir Sp get para obtener informacion del body, si no hay se completa con lo de abajo

    for r in result:
      bookName = r[1]
      bookDescription = r[2]
      bookStars = r[3]
      bookLanguage = r[5]
      bookYear = r[6]
      bookIsbn = r[7]
      bookStock = r[8]
      bookPages = r[9]
      bookPrice = float(r[10])
      bookEditorId = r[12]
      bookAutorId = r[15]
      bookImages = r[4]
      
    if "name" in body:
      args.append(body["name"])
    else:
      args.append(bookName)
    
    if "description" in body:
      args.append(body["description"])
    else:
      args.append(bookDescription)
    
    if "score" in body:
      args.append(body["score"])
    else:
      args.append(bookStars)

    if "language" in body:
      args.append(body["language"])
    else:
      args.append(bookLanguage)
    
    if "releaseYear" in body:
      args.append(body["releaseYear"])
    else:
      args.append(bookYear)

    if "isbn" in body:
      args.append(body["isbn"])
    else:
      args.append(bookIsbn)

    if "stock" in body:
      args.append(body["stock"])
    else:
      args.append(bookStock)
    
    if "pagesNumber" in body:
      args.append(body["pageNumber"])
    else:
      args.append(bookPages)

    if "price" in body and "amount" in body["price"]:
      args.append( body["price"]["amount"])
    else:
      args.append(bookPrice)

    if "editor" in body and "id" in body["editor"]:
      args.append( body["editor"]["id"])
    else:
      args.append(bookEditorId)

    if "autor" in body and "id" in body["autor"]:
      args.append( body["autor"]["id"])
    else:
      args.append(bookAutorId)

    if "image" in body:
      args.append(body["image"])  
    else:
      args.append(bookImages)  

    #Calling the SP to update book info
    consult.modifyBook(args)
    self.statusCode = 204
    self.bodyResponse = None


  def validateRequestBody(self,body):
    pass


    