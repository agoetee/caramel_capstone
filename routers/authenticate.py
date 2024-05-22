"""
Section for authenticating users
"""

from fastapi import APIRouter, Depends, HTTPException, status
from model import schemas, models
from database import get_db
from sqlalchemy.orm import Session
from hashing import Hash
from . import token


api_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@api_router.post("/login")
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    

    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return schemas.Token(access_token=access_token, token_type="bearer")