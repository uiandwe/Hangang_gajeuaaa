# -*- coding: utf-8 -*-
from sqlalchemy import create_engine

from domain.db_class.stock import Stock
from domain.db_class.stock_price import StockPrice
import os


class DataBase:
    now_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        engine = create_engine('sqlite:///'+os.path.join(DataBase.now_path, '../data/stock.db'), echo=True)

        # Base.metadata.create_all(engine)
        Stock.__table__.create(bind=engine, checkfirst=True)
        StockPrice.__table__.create(bind=engine, checkfirst=True)

        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=engine)
        session = Session()

        # stock_list = Stock(name='현승재', code='알케미 테스트', exchange='123qwe')
        # session.add(stock_list)
        # session.commit()

        result = session.query(Stock).all()
        if len(result) > 0:
            for row in result:
                print(row.__dict__)

        # stock_price = StockPrice(Date="2020.03.10", Open=1010.10, High=123.123, Low=100.0, Close=120.10, Volumn=123123,
        #                          stock_id=1)
        # session.add(stock_price)
        # session.commit()

        result = session.query(StockPrice).all()
        if len(result) > 0:
            for row in result:
                print(row.__dict__)

        session.close()


if __name__ == '__main__':
    db = DataBase()

