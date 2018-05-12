import sys
from sqlalchemy import Column, ForeignKey, Integer,\
String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

#configuration
Base = declarative_base()

class Restaurant(Base):
    #table info
    __tablename__ = 'restaurant'

    #mapper
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    #table info
    __tablename__ = 'menu_item'

    #mapper
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


#### insert at end of file ####
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
