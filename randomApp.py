from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Optional, List, Dict

app = FastAPI()

# Simulated in-memory database
fake_db: Dict[int, dict] = {}
next_id = 1

# Pydantic model for Item
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    price: float = Field(..., gt=0)
    tags: Optional[List[str]] = []

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    price: Optional[float] = Field(None, gt=0)
    tags: Optional[List[str]] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the enhanced FastAPI app!"}

@app.get("/items/", response_model=List[Item])
def list_items(skip: int = 0, limit: int = 10):
    items = list(fake_db.values())[skip: skip + limit]
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int = Path(..., ge=1)):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    global next_id
    item_dict = item.dict()
    fake_db[next_id] = item_dict
    next_id += 1
    return item_dict

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: ItemUpdate):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    stored_item = fake_db[item_id]
    updated_item = item_update.dict(exclude_unset=True)
    stored_item.update(updated_item)
    fake_db[item_id] = stored_item
    return stored_item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_db[item_id]
