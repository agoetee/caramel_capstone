from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
import models



api_router = APIRouter(prefix="/api")

#Post request
@api_router.post("/create")
def create_entry(entry: models.Entries, db: Session = Depends(get_db)):
    new_entry = models.Entry(
        create_date=entry.create_date, create_time=entry.create_time, text=entry.text, no_of_calories=entry.no_of_calorie
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

#Get requests 
## Request All Entries
@api_router.get("/entries")
def get_entries_(db_: Session = Depends(get_db)):
    entries_ = db_.query(models.Entry).all()
    return entries_

## Request Single Entry
@api_router.get("/entries/{id}")
def get_one_entry(id: int, db_: Session = Depends(get_db)):
    entry_ = db_.query(models.Entry).filter(models.Entry.id == id).first()
    return entry_