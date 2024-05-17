from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel
from datetime import date, time
from typing import Optional



# Entries Class from BaseModel
class Entries(BaseModel):
    id : int
    create_date: date = None
    create_time: time = None
    text: str
    no_of_calories : float

class UpdateEntries(BaseModel):
    text: Optional[str] = None
    no_of_calories : Optional[float] = None

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer,primary_key=True, autoincrement=True)
    create_date = Column(String)
    create_time = Column(String)
    text = Column(String)
    no_of_calories = Column(Integer)


class ShowEntry(BaseModel):
    text: str
    no_of_calories: float


class UserBase(BaseModel):
    id: int
    name: str
    username: str
    email: str
    password: str


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)


class ShowUser(BaseModel):
    username: str
    email: str


