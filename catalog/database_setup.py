# Setup database
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'app_user'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80))
    picture = Column(String(200))


class Category(Base):
    __tablename__ = 'app_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('app_user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id'    :self.id,
            'name'  :self.name,
        }


class Item(Base):
    __tablename__ = 'app_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(1000), nullable=False)
    image = Column(String(200),nullable=True)
    category_id = Column(Integer, ForeignKey('app_category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('app_user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id'         :self.id,
            'name'       :self.name,
            'description':self.description,
        }


# engine = create_engine('sqlite:///catalog.db')
engine = create_engine('postgresql://student:XUEsheng987@localhost/catalog')

# Base.metadata.drop_all(engine)    # use when schema is changed
Base.metadata.create_all(engine)
