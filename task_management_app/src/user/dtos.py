from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str
    mobile_num: str


class UserResponseSchema(BaseModel):
    name: str
    username: str
    email: str
    mobile_num: str
    id: int
    hash_password: str

class LoginSchema(BaseModel):
    username : str
    password : str
