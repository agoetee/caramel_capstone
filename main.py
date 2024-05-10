from fastapi import FastAPI
import models
from database import engine
from routes import api_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# GET request body

@app.get('/')
def base():
    return {"info": "Hi there"}

app.include_router(api_router)