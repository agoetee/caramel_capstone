"""
Models file contains SQL Alchemy models
"""

from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer,primary_key=True, autoincrement=True)
    create_date = Column(String)
    create_time = Column(String)
    text = Column(String)
    no_of_calories = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))


    users = relationship("User", back_populates="entries")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)


    entries = relationship("Entry", back_populates="users")

