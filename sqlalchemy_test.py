# -*- coding: utf-8 -*-
"""
sqlalchemy 테스트
https://scrolldown.github.io/posts/Python%20tutorial%2007%20-%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A0%80%EC%9E%A5/
https://ulfrid.github.io/python/python-sqlalchemy/
"""

# import sqlite3
# con = sqlite3.connect("data/stock.db")
# type(con)
# cursor = con.cursor()
# create
# cursor.execute("CREATE TABLE stock(id integer primary key autoincrement, name text, code text, exchange text)")
# cursor.execute("CREATE TABLE stock_price(Date text, Open int, High int, Low int, Closing int, Volumn int, stock_id integer, constraint  stock_id_fk foreign key(stock_id) references  stock(id))")

# import pandas as pd
#
# # select
# df = pd.read_sql("SELECT * FROM stock", con, index_col=None)
# print(df)
#
# cursor.execute("INSERT INTO stock VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)")
#
# df = pd.read_sql("SELECT * FROM stock", con, index_col=None)
# print(df)

# con.commit()
# con.close()


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///data/test.db', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(None, ForeignKey('users.id'))
    email_address = Column(String, nullable=False)


# Base.metadata.create_all(engine)
User.__table__.create(bind=engine, checkfirst=True)
Address.__table__.create(bind=engine, checkfirst=True)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# user_list = User(name='현승재', fullname='알케미 테스트', password='123qwe')
# session.add(user_list)
# session.commit()

result = session.query(User).all()
for row in result:
  print(row.__dict__)

# address = Address(user_id=1, email_address='test@test.com')
# session.add(address)
# session.commit()


result = session.query(Address).all()
for row in result:
  print(row.__dict__)


session.close()

