# -*- coding: utf-8 -*-
from domain.database import DataBase
from domain.stock import Stock
from domain.db_class.stock_price import StockPrice
from domain.db_class.stock import Stock as StockModel


def get_kospi_list():
    return Stock().get_stock_code_kospi()


def save_stock_company_info(insert_data):
    return DataBase(echo=False).insert(insert_data)


def get_stock_company_from_code(code):
    return DataBase(echo=False).stock_select_code(code)


def get_stock_company_all():
    return DataBase(echo=False).stock_select_all()


def database_close():
    return DataBase(echo=False).close()


def set_stock_model(obj):
    return StockModel(**obj)


def get_stock(code, start, end):
    return Stock().get_stock_from_pdr_yahoo(code, start, end)


def set_stock_price_model(obj):
    return StockPrice(**obj)
