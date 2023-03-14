from ..database.Model import Item
from ..database.Database import saveItemToDb
class ItemService:

    def getAllItems(self):
        # SQL Alchemy
        return 0

    def createNewItem(self, item:Item):
        if validate(item):
           return saveItemToDb(item)

def validate(item:Item) -> bool:
    if item.value is None:
        return False
    elif item.name is None:
        return False
    else :
        return True