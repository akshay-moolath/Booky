from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime

#user create schema 
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    
#user info schema
class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class LoginSchema(BaseModel):
    username: str
    password: str

#book create,update,view schemas
class BookBase(BaseModel):
    title: str
    content: str
    author_name: str
class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str
    content: Optional[str]

class BookOut(BaseModel):
    id: int
    title: str
    content: str
    author_name:str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    class Config:#read sql object attributes and map to pydantic
        orm_mode = True


