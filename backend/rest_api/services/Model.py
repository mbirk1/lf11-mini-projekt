from typing import List

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Table


class Price():
    id :int
    gold :int
    silver :int
    copper :int


class Item():
    id :int
    name : str
    value: Price


class Purchase():
    id: int
    value: Price
    items: [Item]


class Sale():
    id: int
    value: Price
    items: [Item]