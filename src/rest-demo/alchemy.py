from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from food import Food, create_alchemy_tables

engine = create_engine('mysql://alchemy:alchemy@34.224.209.192/alchemy')

create_alchemy_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()

food = Food(name='steak', description='miam', category='viande')

session.add(food)
session.commit()
