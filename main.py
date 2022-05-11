from fastapi import FastAPI, Query, Path
from typing import Optional
from pydantic import BaseModel
from enum import Enum
from fastapi.responses import FileResponse

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def read_root(name: Optional[str] = Query(None, min_length=4)):
    if name:
        return {"mensaje": f"Hola {name}. Atte: Christos"}
    return {"mensaje": "Hola malditos. Atte: Christos"}

@app.get("/models/{model_name}")
async def get_models(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name":"Es alexnet"}
    else:
        if model_name.value == ModelName.resnet:
            return {"model_name":"Es resnet"}
        else:
            return {"model_name":"Es lenet"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items")
async def post_item(item: Item):
    if item.tax:
        item_dict = item.dict()
        item_dict.update({"total": item.price + item.tax})
        return item_dict
    return item

@app.get("/code")
async def get_code():
    return FileResponse("./main.py")
