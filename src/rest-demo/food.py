from sqlalchemy import Column, Integer, String, Sequence, Enum
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base

alchemy_metadata = MetaData()

Object = declarative_base()

food = Table(
    'food', alchemy_metadata,
    Column('id', Integer, Sequence('food_id'), primary_key=True),
    Column('name', String(50)),
    Column('description', String(255)),
    Column('category', Enum('fruit', 'viande food', 'viande', 'milked product'))
)

class Food(object):
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

mapper(Food, food)

def create_alchemy_tables(engine):
    alchemy_metadata.create_all(engine)
