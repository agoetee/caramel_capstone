from fastapi import FastAPI
from model import models
from database import engine
from routers import entries, user

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# GET request body

@app.get('/')
def base():
    return {"info": "Hi there"}

app.include_router(entries.api_router)
app.include_router(user.api_router)