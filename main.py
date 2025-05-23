from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return{"message": "welcome to tea House"}

@app.get("/teas")
def read_tea():
    return teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    if tea.id == tea_id:
        teas[index] = update_tea
        return update_tea
    return{"error": "Tea not found"}

@app.put("/about")
def about():
    return "This is the crash course content from ChaiAurCode Channels FastAPI course materials"

@app.put("/demo")
def demo_fun():
    return "This is the demo page just to create multile handlers"

@app.put("/random")
def demo_fun():
    return "Just a random handler"

@app.put("/place")
def place_fun():
    return "Just a random placeHolder"

@app.put("/place")
def place_fun():
    return "Just a random placeHolder"
