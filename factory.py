# -*- coding: utf-8 -*-
from domain.database import DataBase
from domain.stock import Stock
from domain.db_class.stock import Stock as StockModel


def get_kospi_list():
    return Stock().get_stock_code_kospi()


def save_stock_company_info(insert_data):
    return DataBase().insert(insert_data)


def database_close():
    return DataBase().close()


def set_stock_model(obj):
    return StockModel(**obj)
