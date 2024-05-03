from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datetime import date, time

from database import Base

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    create_date = Column(String)
    create_time = Column(String)
    text = Column(String)
    no_of_calories = Column(Integer)

