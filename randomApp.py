from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for POST request data
class Item(BaseModel):
    name: str
    description: str = None
    price: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# GET endpoint with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# POST endpoint to create an item
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
