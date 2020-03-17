# -*- coding: utf-8 -*-
from factory import get_kospi_list, set_stock_model, save_stock_company_info, database_close, \
    get_stock_company_from_code
import pandas as pd


class DataController:
    def save_stock_list(self, type='kospi'):
        if type == 'kospi':
            stock_company_list = get_kospi_list()
        else:
            stock_company_list = get_kospi_list()

        for i, row in stock_company_list.iterrows():
            if len(get_stock_company_from_code(row['종목코드'])) > 0:
                pass
            else:
                model = set_stock_model({"name": row['회사명'], "code": row['종목코드'], "exchange": type, "product": row['주요제품']})
                save_stock_company_info(model)

        database_close()


# TODO 모든 국내 주식에 대한 정보 디비로 넣기
if __name__ == '__main__':
    dc = DataController()
    dc.save_stock_list('kospi')

