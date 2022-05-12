
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
| data[n] | |
| data[n].id | Book unique identifier. |
| data[n].name | Book name |
| data[n].description | Book summary |
| data[n].stars | Calification customers made for the book. |
| data[n].images[n] | Book images |
| data[n].images[n].address| URL where the image is stored. |
| data[n].language| Language the book was writen. |
| data[n].isbn| Book ISBN code. |
| data[n].stock| Current stock. |
| data[n].pagesNumber| Book page number. |
| data[n].priceInformation| Book selling price. This amount contains all the taxes or fees. |
| data[n].priceInformation.amount| Monetary amount. |
| data[n].priceInformation.currency| ISO 4217 |

  
### Example:

  

#### With no query parameters


```json
{
	"data": {
		"id": "b001"
	}
}
```  
  

#### With query parameters