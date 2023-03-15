import yaml
from sqlalchemy import create_engine, insert
from ..database.Model import Item

with open("config.yml", "r") as file:
    config_data = yaml.load(file)

engine = create_engine(f'postgresql+psycopg2://{config_data["user"]}:{config_data["password"]}@{config_data["hostname"]}/{config_data["db_name"]}')

def saveItemToDb(item:Item)-> int:
    stmt = insert(tab_api_item).values(name=item.name, value = item.value, price_value = item.price_value)