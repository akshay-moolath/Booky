from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime

#user create schema 
class UserCreate(BaseModel):
    username: str
    password: str
#user info schema
class UserOut(BaseModel):
    id: int
    username: str

    class Config:#read sql object attributes and map to pydantic
        orm_mode = True
#need to use after the login,only name is needed       
class UserMe(BaseModel):
    username: str

#article create,update,view schemas
class ArticleBase(BaseModel):
    title: str
    content: str
class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(BaseModel):
    title: str
    content: Optional[str]

class ArticleOut(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    class Config:
        orm_mode = True


