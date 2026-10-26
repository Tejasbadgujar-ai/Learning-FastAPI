# Create First FastAPI Server & GET Endpoint

## 1. Import FastAPI

```python
from fastapi import FastAPI
```

* We import the FastAPI class from the FastAPI package.
* This class helps us create a FastAPI application.

## 2. Create a FastAPI Application

```python
app = FastAPI()
```

* We create an application object using the FastAPI class.
* We use the `app` object to define routes and endpoints.

## 3. Create a GET Endpoint

```python
@app.get("/")
def home):
    return "Welcome to FastAPI series"
```

* `@app.get("/")` defines a GET endpoint for the root path.
* `def home()` creates a Python function named `home`.
* When a GET request comes to `/`, the `home()` function runs.
* The `return` statement sends the message as the response.

## 4. Create Another Route

```python
@app.get("/contact")
def contact():
    return "You Can Connect Us Any Time"
```

* `/contact` is a different path.
* When a GET request comes to `/contact`, the `contact()` function runs.
* It returns the contact message.

## 5. Run the FastAPI Server

```powershell
fastapi dev main.py
```

* This command starts the FastAPI development server.
* The terminal displays the local server URL.
* We can open the URL in a browser to test the application.

## 6. Test the Endpoints

* `http://127.0.0.1:8000/` displays the home message.
* `http://127.0.0.1:8000/contact` displays the contact message.

## What I Learned

* How to import FastAPI.
* How to create a FastAPI application.
* How to define GET endpoints.
* How to connect routes with Python functions.
* How to return messages from functions.
* How to run and test a FastAPI development server.
