# Implement POST, PUT & DELETE Methods in FastAPI

In this video, I learned how to create, update and delete products using FastAPI. I also learned how to validate product data using Pydantic.

## 1. Files Used

* **main.py:** I implemented the POST, PUT and DELETE endpoints in this file.
* **dtos.py:** I created a `ProductDTO` class to define and validate product data.
* **mockdata.py:** I used the existing `products` list to store product data temporarily.

## 2. ProductDTO and Pydantic Validation

I created a `ProductDTO` class using Pydantic's `BaseModel`.

```python
from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    title: str
    price: int = 0
    count: int = 0
```

**What I learned:**

* `id: int` means the ID must be an integer.
* `title: str` means the title must be a string.
* `price: int = 0` means the price is an integer and defaults to 0 if not provided.
* `count: int = 0` means the count defaults to 0 if not provided.

Pydantic validates incoming data according to the model. For example, if the required `title` field is missing, FastAPI returns a validation error.

## 3. POST Method — Create a Product

I created the `/create_product` endpoint using the POST method.

**What I learned:**

* `product_data: ProductDTO` validates the incoming product data.
* `model_dump()` converts the Pydantic model into a Python dictionary.
* `append()` adds the new product to the end of the products list.

**Example:**

If I send a new product through Postman, the endpoint validates the data and adds it to the list.

```python
product_data = product_data.model_dump()
products.append(product_data)
```

## 4. PUT Method — Update a Product

I created the `/update_product/{product_id}` endpoint using the PUT method.

**What I learned:**

* `product_id` identifies which product I want to update.
* `enumerate(products)` provides both the index and the product while looping through the list.
* `oneProduct.get("id")` gets the product's ID so I can compare it with the requested ID.
* `model_dump()` converts the updated product data into a dictionary.
* `products[index] = ...` replaces the existing product at that index.

**Example:**

If I want to update product ID 2, I send the updated product details through Postman using a PUT request.

## 5. DELETE Method — Delete a Product

I created the `/delete_product/{product_id}` endpoint using the DELETE method.

**What I learned:**

* I use `product_id` to identify the product to delete.
* I use `enumerate()` to get the product's index and data.
* `pop(index)` removes the product at the specified index and returns the removed product.

**Example:**

If I want to delete product ID 2, the endpoint searches for that product and removes it from the list.

```python
deleted_product = products.pop(index)
```

I can use `deleted_product` in the response to show which product was removed.

## 6. Testing with Postman

I learned to test these endpoints using Postman.

* **POST:** Create a product.
* **PUT:** Update an existing product.
* **DELETE:** Delete a product.

I send the product data in JSON format for POST and PUT requests.

## What I Learned in This Video

* How to implement POST, PUT and DELETE endpoints in FastAPI.
* How to define product fields using Pydantic's `BaseModel`.
* How Pydantic validates incoming data.
* How `model_dump()` converts a model into a dictionary.
* How `append()` adds an item to a list.
* How `enumerate()` provides an index and an item.
* How `pop()` removes an item from a list.
* How to test API requests using Postman.

