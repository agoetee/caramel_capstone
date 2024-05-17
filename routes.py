from fastapi import APIRouter,Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
import models, hashing





api_router = APIRouter(prefix="/api")

#Post request
@api_router.post("/create", response_model=models.ShowEntry)
def create_entry(entry: models.Entries, db: Session = Depends(get_db)):
    new_entry = models.Entry(
        create_date=entry.create_date, create_time=entry.create_time, text=entry.text, no_of_calories=entry.no_of_calories
    )
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry

#Get requests 
## Request All Entries
@api_router.get("/entries")
def get_entries_(db: Session = Depends(get_db)):
    entries = db.query(models.Entry).all()
    return entries

## Request Single Entry
@api_router.get("/entries/{id}", status_code=201)
def get_one_entry(id: int, db: Session = Depends(get_db)):
    entry = db.query(models.Entry).filter(models.Entry.id == id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

## Delete Single Entry
@api_router.delete("/entry/{id}")
def delete_one_entry(id: int, db: Session = Depends(get_db)):
    entry = db.query(models.Entry).filter(models.Entry.id == id).first()
    if entry:
        db.delete(entry)
        db.commit()
        return {"message": "Entry deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

## Full Update or Put request
@api_router.put("/entry/{id}")
def update_one_entry(id: int, entry: models.UpdateEntries, db: Session = Depends(get_db)):
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

"""
USERS ROUTES
"""



@api_router.post("/users", response_model=models.ShowUser)
def create_user(entry: models.UserBase, db: Session = Depends(get_db)):
    new_user = models.User(
        name=entry.name, username=entry.username, email=entry.email, password=hashing.Hash.bcrypt(entry.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@api_router.get("/users/{id}")
def get_user(id: int, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user
    