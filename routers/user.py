"""
Contains endpoint for users
"""

from fastapi import APIRouter,Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
import hashing
from model import models, schemas

api_router = APIRouter(
    prefix="/users", 
    tags=["users"]
    )


"""
USERS ROUTES
"""

@api_router.post("/", response_model=schemas.ShowUser)
def create_user(entry: schemas.UserBase, db: Session = Depends(get_db)):
    new_user = models.User(
        name=entry.name, username=entry.username, email=entry.email, password=hashing.Hash.bcrypt(entry.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@api_router.get("/{id}")
def get_user(id: int, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user
    