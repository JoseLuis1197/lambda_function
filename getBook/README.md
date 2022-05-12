
# getBook

  

## Endpoint

    GET /books/{book-id}

  
## Request

### Query params
  

None

### Path params
  

| Field | Description |
|--|--|
| book-id | Unique book identifier. |
  
## Response


This endpoint retrieves the information of a book. If no book is found the data object will be returned empty.


### Body:

| Field | Description |
|--|--|
| data | |
| data.id | Book unique identifier. |
| data.name | Book name |
| data.description | Book summary |
| data.stars | Calification customers made for the book. |
| data.images[n] | Book images |
| data.images[n].address| URL where the image is stored. |
| data.language| Language the book was writen. |
| data.isbn| Book ISBN code. |
| data.stock| Current stock. |
| data.pagesNumber| Book page number. |
| data.priceInformation| Book selling price. This amount contains all the taxes or fees. |
| data.priceInformation.amount| Monetary amount. |
| data.priceInformation.currency| ISO 4217 |

 

### Example:

  

#### With no query parameters

    {
	    "data": {
			"id": "b001"
		}
	}

  
  

#### With query parameters