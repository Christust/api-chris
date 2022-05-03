from fastapi import FastAPI
from typing import Optional

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

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
