from pydantic import BaseModel, EmailStr

from typing import Optional
from pydantic.types import conint
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# this is to check and determine the response that the api sends

class UserCreate(BaseModel):
    id: int
    email: EmailStr
    # add this so as to be able to retrieve the created data
    class Config:
        orm_mode = True
    

class Users(BaseModel):
    email: EmailStr
    password: str
class Postresponse(BaseModel):
    id: int =None
    title: str = None
    content: str = None
    published: bool = True
    owner_id: int = None
    owner: UserCreate = None
    class Config:
        orm_mode = True
# in python you can do inheritance classes
#check the response  
class Detailpost(BaseModel):
    id: int
    title: str
    content: str
    published: bool = True
    owner_id: int
    owner: UserCreate

class Postout(BaseModel):
    Post: Postresponse
    votes: int

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token:str
    token_type:str

class Tokendata(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
