# -*- coding: utf-8 -*-
from factory import get_kospi_list, set_stock_model, save_stock_company_info, database_close, \
    get_stock_company_from_code, get_stock_company_all, get_stock, set_stock_price_model
import pandas as pd
from datetime import datetime


class DataController:
    def save_stock_company_list(self, type='kospi'):
        if type == 'kospi':
            stock_company_list = get_kospi_list()
        else:
            stock_company_list = get_kospi_list()

        for i, row in stock_company_list.iterrows():
            if len(get_stock_company_from_code(row['종목코드'])) > 0:
                pass
            else:
                model = set_stock_model({"name": row['회사명'], "code": row['종목코드'], "exchange": type, "product": row['주요제품'], "listed_date": row['상장일']})
                save_stock_company_info(model)

    def save_stock_to_company(self):
        result = get_stock_company_all()
        today = datetime.today().strftime('%Y-%m-%d')
        for data in result:
            print(data)

            start = datetime.strptime(data.listed_date, "%Y-%m-%d").date()
            code = data.code

            stock_data = get_stock(code, start, today)
            stock_data['Date'] = stock_data.index
            stock_id = data.id

            for i, row in stock_data.iterrows():
                stock_price_model = set_stock_price_model({"Date": row['Date'].strftime('%Y-%m-%d'), "Open": row["Open"], "High": row['High'],
                                                           "Low": row["Low"], "Close": row["Close"],
                                                           "Volume": row["Volume"], "stock_id": stock_id})
                save_stock_company_info(stock_price_model)


# TODO 모든 국내 주식에 대한 정보 디비로 넣기
if __name__ == '__main__':
    dc = DataController()
    dc.save_stock_company_list('kospi')
    dc.save_stock_to_company()
    database_close()

