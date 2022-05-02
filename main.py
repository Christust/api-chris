from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola mundo"}

@app.get("/item/{item_id}")
async def foo(item_id: int):
    return {"item_id":item_id}