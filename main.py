from fastapi import FastAPI   # create a class 

app = FastAPI() 

#suppose use in (/home) so thats your url is http//:127.0.0.1:8000/home that after showing that message 

@app.get("/")  #  / is the present text showing  
def home(): # create function to return message
    return "welcome to FastAPI series"

#also create practice

@app.get("/contact") #these is rout and not repeat same rout so every page different rout to understanding easily
def contact():
     
     return "You Can Connect Us Any Time"

