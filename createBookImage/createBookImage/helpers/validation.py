
class validation:

  def __init__(self) -> None:
      self.status = ""
      self.validationResponse = []
  
  def validateCreationBookRequest(self,body):
    ##Adding name

    if "name" in body:
        self.validationResponse.append(body["name"])           
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo name no ha sido informado."]
        return validation

    #Adding description
    if "description" in body:
        self.validationResponse.append(body["description"])        

    self.validationResponse.append(0)

    self.validationResponse.append("")

    #Adding language
    if "language" in body:
        self.validationResponse.append(body["language"])        

    #Adding release year
    if "releaseYear" in body:
        self.validationResponse.append(body["releaseYear"])        

    #Adding isbn code
    if "isbn" in body:
        self.validationResponse.append(body["isbn"])        

    self.validationResponse.append(0)  

    #Adding pages number
    if "pagesNumber" in body:
        self.validationResponse.append(body["pagesNumber"])        

    #Adding book price
    if "price" in body and "amount" in body["price"]:
        self.validationResponse.append(body["price"]["amount"])        
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo price.amount no ha sido informado."]
        return validation

    #Adding editor id
    if "editor" in body and "id" in body["editor"]:
        self.validationResponse.append(body["editor"]["id"])         
    else:
        self.status = "WRONG"
        self.validationResponse = []
        self.validationResponse = ["requiredFieldMissing","El campo editor.id no ha sido informado."]
        return validation

    #Adding autor id
    if "autor" in body and "id" in body["autor"]:
        self.validationResponse.append(body["autor"]["id"])
        self.status = "OK"  
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo autor.id no ha sido informado."]
        return validation

    self.status = "OK"

    return validation