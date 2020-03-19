# -*- coding: utf-8 -*-
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.db_class.stock import Stock
from domain.db_class.stock_price import StockPrice
from domain.singleton import Singleton


class DataBase(metaclass=Singleton):
    now_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, echo=True):
        engine = create_engine('sqlite:///'+os.path.join(DataBase.now_path, '../data/stock.db'), echo=echo)
        # Base.metadata.create_all(engine)
        Stock.__table__.create(bind=engine, checkfirst=True)
        StockPrice.__table__.create(bind=engine, checkfirst=True)

        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self, insert_data):
        try:
            self.session.add(insert_data)
            self.session.commit()
        except Exception as e:
            print(e)

    def select(self):
        result = self.session.query(Stock).all()
        if len(result) > 0:
            for row in result:
                print(row.__dict__)

        result = self.session.query(StockPrice).all()
        if len(result) > 0:
            for row in result:
                print(row.__dict__)
        pass

    def stock_select_name(self, name):
        result = self.session.query(Stock).filter(Stock.name == name)
        return result.all()

    def stock_select_code(self, code):
        result = self.session.query(Stock).filter(Stock.code == code)
        return result.all()

    def stock_select_all(self):
        result = self.session.query(Stock).all()
        return result

    def close(self):
        self.session.close()


if __name__ == '__main__':
    db = DataBase(False)
    db.select()
    # stock_list = Stock(name='현승재', code='알케미 테스트', exchange='123qwe')
    # stock_price = StockPrice(Date="2020.03.10", Open=1010.10, High=123.123, Low=100.0, Close=120.10, Volumn=123123, stock_id=1)
    # db.insert(stock_price)
    db.select()
    db.close()

