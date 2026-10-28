## Path Parameters and Query Parameters in FastAPI

## 1. Start the Server

I can start the FastAPI server with:

```bash
fastapi dev main.py
```

After the server starts, I can test the endpoints in a browser or API client.

## 2. Path Parameters

A path parameter is part of the URL. I used `product_id` to find one product by its ID.

```python
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"error": "Product not found for this id"}
```

`{product_id}` is a dynamic value in the path.

`product_id: int` tells FastAPI that the value should be an integer.

The function checks the product list and returns the matching product.

**Example URL:**

`http://127.0.0.1:8000/product/1`

## 3. Query Parameters

Query parameters are written after `?` in a URL. In the original practice code, I used `Request` and `request.query_params` to read them.

```python
@app.get("/greet")
def greet_user(request: Request):
    query_parameter = dict(request.query_params)

    return {
        "greet": f"Hello {query_parameter.get('name')}, "
                 f"Your age is {query_parameter.get('age')}"
    }
```

**Example URL:**

`http://127.0.0.1:8000/greet?name=Tejas&age=20`

This version reads query parameters from the request and converts them to a dictionary.

## 4. Path Parameters vs Query Parameters

**Path parameter example:**

`/product/1`

**Query parameter example:**

`/greet?name=Tejas&age=20`

Path parameters are part of the URL path. Query parameters appear after `?`.

## 5. Code Review Update: Typed Query Parameters

During the code review, I replaced the manual `Request` handling with FastAPI's typed query parameters, as requested in the review.

```python
@app.get("/greet")
def greet_user(name: str, age: int = 21):
    return {
        "greet": f"Hello {name}, your age is {age}"
    }
```

`name: str` makes `name` a required string query parameter.

`age: int = 21` makes `age` an integer and gives it a default value of `21`.

FastAPI validates the query parameters automatically.

**Example URL with a valid age:**

`/greet?name=Tejas&age=20`

**Example URL using the default age:**

`/greet?name=Tejas`

In this case, the age defaults to `21`.

**Example URL with an invalid age:**

`/greet?name=Tejas&age=abc`

This request returns a `422` validation error because `abc` is not an integer.

## 6. Code Review Update: Not-Found Response

The product-by-ID endpoint was updated to return an actual HTTP `404` response when a product is missing, instead of returning an error dictionary with status `200`.

```python
raise HTTPException(
    status_code=404,
    detail="Product not found"
)
```

This allows the API to return the correct not-found status when the requested product does not exist.

## 7. What I Practiced

* Starting the FastAPI server.
* Finding a product by its ID.
* Passing values through query parameters.
* Using typed query parameters and automatic validation.
* Returning a `404` status when a requested product does not exist.
