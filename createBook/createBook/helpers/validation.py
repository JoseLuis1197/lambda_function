class validation:

  def __init__(self) -> None:
      self.status = ""
      self.validationResponse = []
  
  def validateCreationBookRequest(self,body):
    ##Adding name

    if body["name"]:
        self.validationResponse.append(body["name"])
        self.status = "OK"     
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo name no ha sido informado."]

    #Adding description
    if body["description"]:
        self.validationResponse.append(body["description"])
        self.status = "OK"  
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo description no ha sido informado."]
    
    self.validationResponse.append(0)

    self.validationResponse.append("")

    #Adding language
    if body["language"]:
        self.validationResponse.append(body["language"])
        self.status = "OK"  
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo language no ha sido informado."]

    #Adding release year
    if body["releaseYear"]:
        self.validationResponse.append(body["releaseYear"])
        self.status = "OK"  
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo releaseYear no ha sido informado."]

    #Adding isbn code
    if body["isbn"]:
        self.validationResponse.append(body["isbn"])
        self.status = "OK"  
    else:
        self.status = "WRONG"
        self.validationResponse = []

    self.validationResponse.append(0)  

    #Adding pages number
    if body["pagesNumber"]:
        self.validationResponse.append(body["pagesNumber"])
        self.status = "OK" 
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo pagesNumber no ha sido informado."]

    #Adding book price
    if body["price"]["amount"]:
        self.validationResponse.append(body["price"]["amount"])
        self.status = "OK"  
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo price.amount no ha sido informado."]

    #Adding editor id
    if body["editor"]["id"]:
        self.validationResponse.append(body["editor"]["id"])
        self.status = "OK"  
    else:
        self.status = "WRONG"
        self.validationResponse = []
        self.validationResponse = ["requiredFieldMissing","El campo editor.id no ha sido informado."]


    #Adding autor id
    if body["autor"]["id"]:
        self.validationResponse.append(body["autor"]["id"])
        self.status = "OK"  
    else:
        self.status = "WRONG"
        self.validationResponse = ["requiredFieldMissing","El campo autor.id no ha sido informado."]

    return validation