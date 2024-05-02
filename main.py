from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date, time


app = FastAPI()

class Entries(BaseModel):
    create_date: date
    create_time: time
    text: str
    no_of_calorie : float


@app.get('/')
def base():
    return {"info": "Hi there"}

#Post request

@app.post('/create')
def create_entry(post: Entries):
    return {
        "maker": [
            {"create date": post.create_date},
            {"create time": post.create_time},
            {"info": post.text},
            {"calory": post.no_of_calorie}
            ]
        }