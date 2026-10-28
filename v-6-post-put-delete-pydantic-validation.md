## Implement POST, PUT, DELETE and Pydantic Validation

In this video, I learned how to create, update, and delete products using FastAPI. I also learned how to validate product data using Pydantic and test API endpoints with Postman.

## 1. Files Used

* `main.py` — I created the API endpoints in this file.
* `dtos.py` — I defined the `ProductDTO` class for product validation.
* `mockdata.py` — I stored sample product data in a Python list.

## 2. ProductDTO and Pydantic

I created a `ProductDTO` class using Pydantic's `BaseModel`.

```python
from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    title: str
    price: int = 0
    count: int = 0
```

Here, `id` should be an integer and `title` should be a string. The price and count have default values of `0`.

FastAPI uses this model to validate the data received from POST and PUT requests.

## 3. POST Method — Create a Product

I used the POST method to add a new product to the product list.

```python
new_product = product_data.model_dump()
products.append(new_product)
return new_product
```

`model_dump()` converts the Pydantic model into a dictionary, and `append()` adds the new product to the list.

During code review, I added a check to prevent duplicate product IDs. If the ID already exists, the API returns `400 Bad Request`. When a product is created successfully, it returns `201 Created`.

For example, I can send a product with an ID, title, price, and count through Postman.

## 4. PUT Method — Update a Product

I used PUT to update an existing product by its ID.

```python
updated = product_data.model_dump()
updated["id"] = product_id
products[index] = updated
return updated
```

I used `enumerate(products)` to get the index and product while searching the list. After finding the product, I update it at the same index.

During code review, I fixed an issue where the ID from the request body could replace the product ID in the URL. Now, the URL ID takes priority.

For example, if the URL contains `/update_product/1` but the request body contains `"id": 5`, the updated product keeps ID `1`.

If the product does not exist, the API returns `404 Not Found`.

## 5. DELETE Method — Delete a Product

I used DELETE to remove a product from the list.

```python
deleted_product = products.pop(index)
return deleted_product
```

`pop(index)` removes the product and returns the removed item.

During code review, I changed the response to return the actual deleted product instead of an empty object. If the product is not found, the API returns `404 Not Found`.

## 6. GET Method — Handle Missing Products

I used the GET endpoint `/product/{product_id}` to find a product by its ID.

During code review, I changed the not-found response to use `HTTPException`.

```python
raise HTTPException(
    status_code=404,
    detail="Product not found"
)
```

Earlier, the endpoint returned an error dictionary with status `200 OK`. Now, it correctly returns `404 Not Found` when the product does not exist.

I also applied the same not-found handling to the PUT and DELETE endpoints.

## 7. Query Parameters in `/greet`

I updated the `/greet` endpoint to use typed query parameters.

```python
@app.get("/greet")
def greet_user(name: str, age: int = 21):
    return {
        "greet": f"Hello {name}, your age is {age}"
    }
```

Here, `name` is a string and `age` is an integer with a default value of `21`.

For example, `/greet?name=Tejas&age=21` returns a greeting. If I pass `age=abc`, FastAPI returns a `422` validation error because the age should be an integer.

## 8. Testing with Postman

I tested the endpoints using Postman:

* GET — retrieve existing and missing products.
* POST — create a product and check duplicate IDs.
* PUT — update a product and check that the URL ID is preserved.
* DELETE — delete a product and check the response.
* `/greet` — test valid and invalid query parameters.

I checked the expected HTTP status codes, including `201`, `400`, `404`, and `422`.

## What I Learned

I learned how to implement CRUD operations, validate product data with Pydantic, use `model_dump()`, `append()`, `enumerate()`, and `pop()`, and return appropriate HTTP status codes.

**Note:** The products are stored in a Python list, so the changes are temporary and are not permanently saved in a database.
