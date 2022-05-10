from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"mensaje": "Hola malditos. Atte: Christos"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
