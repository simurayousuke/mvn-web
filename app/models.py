from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


# 得到base-model
base = declarative_base()


class User(base):
    __tablename__ = 'user'
    id = Column(String(10), primary_key=True)
    name = Column(String(10))
    age = Column(String(10))

    def __init__(self):
        pass

    def __repr__(self):
        pass