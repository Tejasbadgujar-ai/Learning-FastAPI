from fastapi import FastAPI,Request  # create a class 
from mockdata import products

app = FastAPI() 

#suppose use in (/home) so thats your url is http//:127.0.0.1:8000/home that after showing that message 

@app.get("/")  #  / is the present text showing  
def home(): # create function to return message
    return "welcome to FastAPI series"

#also create practice

@app.get("/contact") #these is rout and not repeat same rout so every page different rout to understanding easily
def contact():
     
     return "You Can Connect Us Any Time"


#they return product data in mockup file and also display to  with url in chrome http:127.0.0.1.8000
@app.get("/products")
def get_products():
     
     return products



## path paramerers

@app.get("/product/{product_id}")   #{} define value in dynamic value  product_id is dynamic value
def get_one_product(product_id:int): #product_id is tring or int that can define him the parameter
     
## if product available with the id, return product, else return error message.
     for oneProduct in products:
          if oneProduct.get("id") ==  product_id:
               return oneProduct

     return {
          "error": "Product not found for this id"
     }


## query parameters

@app.get("/greet")
def greet_user(request: Request):    #name:str,age=21  that like also define him 
     query_parameter = dict(request.query_params)
   
     return {
          "greet": f"Hello {query_parameter.get('name')}, Your age is {query_parameter.get('age')}"
     }