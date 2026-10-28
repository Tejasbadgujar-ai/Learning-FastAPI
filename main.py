from fastapi import FastAPI, HTTPException, status  
from mockdata import products 
from dtos import ProductDTO

app = FastAPI() 

# home route
@app.get("/")    
def home(): 
    return "welcome to FastAPI series"


# contact route
@app.get("/contact") 
def contact():
     
     return "You Can Connect Us Any Time"


# get_product route
@app.get("/products")
def get_products():
     
     return products



# path paramerers
# Get product by ID
@app.get("/product/{product_id}")       
def get_one_product(product_id: int):       
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    ) 
  
     
# query parameters
@app.get("/greet")
def greet_user(name: str, age: int = 21):
    return {
        "greet": f"Hello {name}, your age is {age}"
    }

# different types of http method
# Create product
@app.post("/create_product", status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductDTO):
    if any(p["id"] == product_data.id for p in products):
        raise HTTPException(
            status_code=400,
            detail="Product id already exists"
        )

    new_product = product_data.model_dump()
    products.append(new_product)

    return new_product

#enumerate is index and data both provide
# update product
@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO, product_id:int):    

     for index, oneProduct in enumerate(products): 
         if oneProduct.get("id") == product_id:
            updated = product_data.model_dump()
            updated["id"] = product_id
            products[index] = updated
            return updated


     raise HTTPException(
    status_code=404,
    detail="Product not found"
)

#delete method 
@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
     for index, oneProduct in enumerate(products):
          if oneProduct.get("id") == product_id:
              deleted_product = products.pop(index)
              return deleted_product

     raise HTTPException(
    status_code=404,
    detail="Product not found"
)

