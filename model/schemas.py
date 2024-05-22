"""
The schemas file contains Pydantic models
"""

from pydantic import BaseModel
from datetime import date, time
from typing import Optional, List, Union



# Entries Class from BaseModel
class EntriesBase(BaseModel):
    id : int
    create_date: date = None
    create_time: time = None
    text: str
    no_of_calories : float


class Entries(EntriesBase):
    class Config:
        from_attributes = True

class UpdateEntries(BaseModel):
    text: Optional[str] = None
    no_of_calories : Optional[float] = None



class UserBase(BaseModel):
    id: int
    name: str
    username: str
    email: str
    password: str

class ShowUser(BaseModel):
    username: str
    email: str
    entries: List[EntriesBase] = []

    class Config:
        from_attributes = True

class ShowEntry(BaseModel):
    text: str
    no_of_calories: float
    users: ShowUser

    class Config:
        from_attributes = True


class Login(BaseModel):
    username: str
    email: str
    password: str


"""Token Auth"""
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None