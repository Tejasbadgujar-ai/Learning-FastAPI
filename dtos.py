# dtos = data transfer objects 

from pydantic import BaseModel

class ProductDTO (BaseModel):

    id: int
    title: str
    price: int = 0       #define the data int float or any data type 
    count: int = 0        # and default value also writ up 