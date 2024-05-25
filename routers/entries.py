"""
Contains endpoint for calorie Entries
"""

from fastapi import APIRouter,Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from model import models, schemas
from . import oauth2


api_router = APIRouter(
    prefix="/entries", 
    tags=["entries"]
    )

#Post request
@api_router.post("/", response_model=schemas.ShowEntry)
def create_entry(entry: schemas.EntriesBase, db: Session = Depends(get_db)):
    new_entry = models.Entry(
        create_date=entry.create_date, create_time=entry.create_time, text=entry.text, no_of_calories=entry.no_of_calories
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

#Get requests 
## Request All Entries
@api_router.get("/")
def get_entries_(db: Session = Depends(get_db), get_current_user: schemas.UserBase = Depends(oauth2.get_current_user)):
    entries = db.query(models.Entry).all()
    return entries

## Request Single Entry
@api_router.get("/{id}", status_code=201)
def get_one_entry(id: int, db: Session = Depends(get_db)):
    entry = db.query(models.Entry).filter(models.Entry.id == id).first()
    if not entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Entry not found")
    return entry

## Delete Single Entry
@api_router.delete("/{id}")
def delete_one_entry(id: int, db: Session = Depends(get_db)):
    entry = db.query(models.Entry).filter(models.Entry.id == id).first()
    if entry:
        db.delete(entry)
        db.commit()
        return {"message": "Entry deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

## Full Update or Put request
@api_router.put("/{id}")
def update_one_entry(id: int, entry: schemas.UpdateEntries, db: Session = Depends(get_db)):
    update_dict = entry.model_dump(exclude_unset=True)
    the_entry = db.query(models.Entry).filter(models.Entry.id == id).update(update_dict)
    if not the_entry:
        raise HTTPException(status_code=404, detail=f"Entry with id {id} not found")
    db.commit()
    return 'updated'
    
## Help from HUB 
#    try:
#        to_dict = entry.model_dump(exclude_unset=True)
#        db.query(models.Entry).filter(models.Entry.id == id).update(to_dict)
#        db.commit()
#        return {"message": "Entry updated successfully"}
#    except Exception as e:
#        raise HTTPException(status_code=500, detail=str(e))
