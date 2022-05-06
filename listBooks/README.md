
# listBooks

  

## Endpoint:

    GET /books

  
## Request

### Query params:
  

| Field|Description |type |
|--|--|--|
| name | Search by book bame. | string |
| autorName| Search bu autor name. | string |
| limit| Set the maximum quantity of items needed to be returned.| string |
| offset| Next number value | string |

  

## Response:


This endpoint retrieves a list of books. If limit and offset were informed, the endpoint must only retrieves the maximum limit of books.


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