from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel
from datetime import date, time
from typing import Optional, List



# Entries Class from BaseModel
class EntriesBase(BaseModel):
    id : int
    create_date: date = None
    create_time: time = None
    text: str
    no_of_calories : float


class Entries(EntriesBase):
    class Config:
        orm_mode = True

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
    user_id = Column(Integer, ForeignKey("users.id"))


    users = relationship("User", back_populates="entries")


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


    entries = relationship("Entry", back_populates="users")


class ShowUser(BaseModel):
    username: str
    email: str
    entries: List[EntriesBase] = []

    class Config:
        orm_mode = True

class ShowEntry(BaseModel):
    text: str
    no_of_calories: float
    users: ShowUser

    class Config:
        orm_mode = True
