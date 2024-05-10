from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel
from datetime import date, time

# Entries Class from BaseModel
class Entries(BaseModel):
    id : int
    create_date: date = None
    create_time: time = None
    text: str
    no_of_calorie : float

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, Sequence('item_id_seg', start=1),primary_key=True, autoincrement=True)
    create_date = Column(String)
    create_time = Column(String)
    text = Column(String)
    no_of_calories = Column(Integer)

