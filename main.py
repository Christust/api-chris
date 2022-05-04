from optparse import Option
from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def root():
    return {"message": "Hola mundo"}

@app.get("/item/{item_id}")
async def foo(item_id: int):
    return {"item_id":item_id}

@app.get("/items_fake")
async def foo(skip: int = 0, limit: int = 10):
    return {"items_fake":fake_items_db[skip:skip+limit]}

@app.get("/items_optionals/{item_id}")
async def foo(item_id: int, required: bool, no_required: bool = False, optional: Optional[str] = None):
    if optional:
        return {"item_id":item_id, "required":required,"no_required":no_required, "optional":optional }
    return {"item_id":item_id, "required":required,"no_required":no_required}

@app.post("/items")
async def items(item:Item):
    item_dict = item.dict()
    if item.tax:
        item_dict.update({"total":item.price+item.tax})
    return item_dict

@app.put("/items/{item_id}")
async def items(item_id:int, item:Item, needy: str = Query(..., max_length=5 ), q:Optional[str]=Query(None, min_length=2)):
    item_dict = {"item_id":item_id,**item.dict()}
    if q:
        item_dict.update({"optional":q})
    return item_dict
