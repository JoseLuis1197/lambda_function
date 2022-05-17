
# createBook


## Endpoint:

    POST /books

  
## Request

Creates a book.

### Query params:

None

### Body:

| Field | Description |
|--|--|
|name | Book name |
|description | Book summary |
|isbn | ISBN code |
|language | Book language |
|pagesNumber| Book page number. |
|price | Book selling price. This amount contains all the taxes or fees. |
|price.amount | Monetary amount |
|price.currency | String based ISO 4217 |
|editor | Editor information |
|editor.id | Editor identifier |
|autor | Autor information |
|autor.id | Autor identifier |
  
## Response:

### Body:

| Field | Description |
|--|--|
| data.id | Book unique identifier. |
  
### Example:

  
    {
	    "data": {
			"id": "b001"
		}
	}
