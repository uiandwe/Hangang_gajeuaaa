# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    exchange = Column(String)

    def __init__(self, name, code, exchange):
        self.name = name
        self.code = code
        self.exchange = exchange

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.code, self.exchange)
