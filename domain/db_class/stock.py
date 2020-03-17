# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    exchange = Column(String) # kospi / kosdaq
    product = Column(String) # 주요 제품
    listed_date = Column(String) # 상장일

    def __init__(self, name, code, exchange, product, listed_date):
        self.name = name
        self.code = code
        self.exchange = exchange
        self.product = product
        self.listed_date = listed_date

    def __repr__(self):
        return "<Stock('%s', '%s', '%s, %s, %s')>" % (self.name, self.code, self.exchange, self.product, self.listed_date)
