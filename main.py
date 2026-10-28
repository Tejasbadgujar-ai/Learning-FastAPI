from fastapi import FastAPI, HTTPException, status

from mockdata import products
from dtos import ProductDTO


app = FastAPI()


# Home route
@app.get("/")
def home():
    return "welcome to FastAPI series"


# Contact route
@app.get("/contact")
def contact():
    return "You Can Connect Us Any Time"


# Get all products
@app.get("/products")
def get_products():
    return products


# Path parameters
# Get product by ID
@app.get("/product/{product_id}")
def get_one_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found",
    )


# Query parameters
@app.get("/greet")
def greet_user(name: str, age: int = 21):
    return {
        "greet": f"Hello {name}, your age is {age}"
    }


# Create a product
@app.post(
    "/create_product",
    status_code=status.HTTP_201_CREATED,
)
def create_product(product_data: ProductDTO):
    if any(product["id"] == product_data.id for product in products):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product id already exists",
        )

    new_product = product_data.model_dump()
    products.append(new_product)

    return new_product


# Update a product
@app.put("/update_product/{product_id}")
def update_product(product_id: int, product_data: ProductDTO):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            updated = product_data.model_dump()
            updated["id"] = product_id
            products[index] = updated

            return updated

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found",
    )


# Delete a product
@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)
            return deleted_product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found",
    )