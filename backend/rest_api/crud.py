from sqlalchemy.orm import Session
import models, schemas


def getAllItems(db: Session):
    return db.query(models.Item)


def createItem(db: Session, item: schemas.Item):
    priceToCreate = models.Price(gold=item.value.gold, silver=item.value.silver, copper=item.value.copper)
    db.add(priceToCreate)
    db.commit()
    db.refresh(priceToCreate)
    itemToCreate = models.Item(name=item.name, value=priceToCreate.id)
    db.add(itemToCreate)
    db.commit()
    db.refresh(itemToCreate)
    return itemToCreate
