from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def base():
    return {"info": "Hi there"}