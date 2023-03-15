from pydantic import BaseModel
class PriceBase(BaseModel):
    id: int
    gold: int
    silver: int
    copper: int

class Price(BaseModel):
    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    id: int
    name: str
    value: PriceBase

class Item(ItemBase):
    class Config:
        orm_mode = True
