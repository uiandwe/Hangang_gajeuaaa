# -*- coding: utf-8 -*-
from domain.database import DataBase
from domain.stock import Stock
from domain.db_class.stock_price import StockPrice
from domain.db_class.stock import Stock as StockModel
from domain.controller.data_controller import DataController


def get_kospi_list():
    return Stock().get_stock_code_kospi()


def get_korea_stock_list():
    return Stock().get_stock_code_kr()


def save_stock_company_info(insert_data):
    return DataBase(echo=False).insert(insert_data)


def get_stock_company_from_code(code):
    return DataBase(echo=False).stock_select_code(code)


def get_stock_company_all():
    return DataBase(echo=False).stock_select_all()


def database_close():
    return DataBase(echo=False).close()


def get_stock_company_from_name(name):
    return DataBase(echo=False).stock_select_name(name)


def set_stock_model(obj):
    return StockModel(**obj)


def get_stock(code, start=None, end=None):
    return Stock().get_stock_from_fdr(code, start, end)


def set_stock_price_model(obj):
    return StockPrice(**obj)


def get_company_from_name_to_data(company_name):
    return DataController(get_stock_company_from_name=get_stock_company_from_name, get_stock=get_stock).\
        get_company_name_code(company_name)
