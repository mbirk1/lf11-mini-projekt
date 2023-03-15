from typing import List

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Table


class Base(DeclarativeBase):
    pass

tab_api_purchase_items = Table(
    "tab_api_purchase_items",
    Base.metadata,
    Column("purchase_id", ForeignKey("tab_api_purchase.id")),
    Column("item_id", ForeignKey("tab_api_item.id"))
)

tab_api_sale_items = Table(
    "tab_api_sale_items",
    Base.metadata,
    Column("purchase_id", ForeignKey("tab_api_sale.id")),
    Column("item_id", ForeignKey("tab_api_item.id"))
)

class Price(Base):
    __tablename__ = "tab_api_price"
    id = mapped_column("id", int)
    gold = mapped_column("gold", int)
    silver = mapped_column("silver", int)
    copper = mapped_column("copper", int)


class Item(Base):
    __tablename__ = "tab_api_item"
    id = mapped_column(int, nullable=False, primary_key=True)
    name = mapped_column("item_name", String)
    value= mapped_column(ForeignKey("tab_api_price.id"))
    price_value = relationship("Price", back_populates="item")


class Purchase(Base):
    __tablename__ = "tab_api_purchase"
    id = Column("id", nullable=False, primary_key=True)
    value= mapped_column(ForeignKey("tab_api_price.id"))
    price_value = relationship("Price", back_populates="item")
    items: Mapped[List[Item]] = relationship(secondary=tab_api_purchase_items)


class Sale(Base):
    __tablename__ = "tab_api_sale"
    id: int
    value: Price
    items: Mapped[List[Item]] = relationship(secondary=tab_api_sale_items)