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