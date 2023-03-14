from fastapi import FastAPI
from services.ItemService import ItemService
from database.Model import Item

app = FastAPI()


@app.post("/items/new")
async def createNewItem(item: Item):
        ItemService.createNewItem(item)

@app.get("/items/{itemId}")
async def getItemWithId(itemId: str):
        return {"message": itemId}


@app.get("/items")
async def getAllItems():
        return ItemService.getAllItems()


# https://fastapi.tiangolo.com/tutorial/path-params/
# https://packaging.python.org/en/latest/tutorials/packaging-projects/