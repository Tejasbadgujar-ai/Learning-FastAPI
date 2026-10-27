## Path Parameters & Query Parameters in FastAPI

## 1. Start the Server

First, I started the FastAPI server using this command in the VS Code terminal.

```bash
fastapi dev main.py
```

After starting the server, I opened the URLs in my browser to check the output.

## 2. Path Parameters

I learned how to use path parameters to get a particular product using its ID.

In the URL, `{product_id}` is a dynamic value. We can pass a product ID directly in the URL.

```python
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct

    return {
        "error": "Product not found for this id"
    }
```

Here, `product_id: int` means the product ID should be an integer.

The function checks the products one by one. If the ID matches, it returns that product. Otherwise, it returns an error message.

**Browser URL:**

`http://127.0.0.1:8000/product/1`

## 3. Query Parameters

I learned how to pass values like name and age through the URL and use them in a function.

For this, I used `Request` and `request.query_params`.

```python
@app.get("/greet")
def greet_user(request: Request):
    query_parameter = dict(request.query_params)

    return {
        "greet": f"Hello {query_parameter.get('name')}, Your age is {query_parameter.get('age')}"
    }
```

Here, `request.query_params` gets the values from the URL, and `dict()` converts them into a dictionary.

The `.get()` method helps me access the name and age values.

**Browser URL:**

`http://127.0.0.1:8000/greet?name=Tejas&age=20`

**Output:**

```json
{
    "greet": "Hello Tejas, Your age is 20"
}
```

## 4. Path Parameters vs Query Parameters

**Path Parameters:** I used a path parameter to get a product using its ID.

Example: `/product/1`

**Query Parameters:** I used query parameters to pass the name and age through the URL.

Example: `/greet?name=Tejas&age=20`

The main difference is that path parameters are part of the URL path, while query parameters come after the `?` symbol.

## 5. What I Practiced

* Starting the FastAPI server using `fastapi dev main.py`.
* Getting a product using its ID with a path parameter.
* Returning an error message when a product ID is not found.
* Passing name and age through query parameters.
* Getting query parameter values using `request.query_params`.
* Checking the output in the browser.
