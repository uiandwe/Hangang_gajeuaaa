# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from .stock import Stock
Base = declarative_base()


class StockPrice(Base):
    __tablename__ = 'stock_price'

    id = Column(Integer, primary_key=True)
    Date = Column(String)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Volumn = Column(Float)
    stock_id = Column(Integer, ForeignKey(Stock.id))

    def __init__(self, Date, Open, High, Low, Close, Volumn, stock_id):
        self.Date = Date
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Close = Close
        self.Volumn = Volumn
        self.stock_id = stock_id

    def __repr__(self):
        return "<StockPrice('%s', '%s', '%s')>" % (self.Date, self.Close, self.stock_id)
