# from typing import List, Optional
from pydantic import BaseModel


class URL(BaseModel):
    url: str


class User(BaseModel):
    name: str
    email: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True
