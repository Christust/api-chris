from typing import Union
from fastapi import Body, Depends, FastAPI, Query, Path, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, Required
from enum import Enum
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str = Field(min_length=3)
    description: Union[str, None] = Field(default=None, min_length=3)
    price: float = Field(gt=0)
    tax: Union[float, None] = Field(default=None, gt=0)

@app.get("/")
async def read_root(name: Union[str, None] = Query(default=None, min_length=4)):
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
async def read_item(*, item_id: int = Path(..., title="ID of an item", gt=0, le=1000), q: str):
    return {"item_id": item_id}

@app.post("/items", status_code=status.HTTP_201_CREATED)
async def post_item(item: Item):
    if item.tax:
        item_dict = item.dict()
        item_dict.update({"total": item.price + item.tax})
        return item_dict
    return item

@app.get("/code")
async def get_code():
    return FileResponse("./main.py")

@app.get("/documentation")
async def get_documentation(token: str = Depends(oauth2_scheme)):
    return {"token": token}

# Descomentar para depurar
# uvicorn.run(app, host="0.0.0.0", port=8000)
