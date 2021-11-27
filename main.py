from fastapi import FastAPI
from enum import Enum
import uvicorn
from pydantic import BaseModel

class MyItem(BaseModel):
    subject:str
    description:str

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/insert")
async def insert(item: MyItem):
    print(item)
    return {"text": "Hello Tinh Bui"}


