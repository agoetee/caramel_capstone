from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Entries(BaseModel):
    date: None
    time: None
    text: str
    no_of_calorie : float


@app.get('/')
def base():
    return {"info": "Hi there"}

#Post request

@app.post('/create')
def create_entry(post: Entries):
    """"""