# -*- coding: utf-8 -*-
from factory import get_korea_stock_list, set_stock_model, save_stock_company_info, database_close, \
    get_stock_company_from_code, get_stock_company_all, get_stock, set_stock_price_model
import pandas as pd
from datetime import datetime


class DataController:
    def save_stock_company_list(self):
        stock_company_list = get_korea_stock_list()

        for i, row in stock_company_list.iterrows():
            listing_date = None
            if not pd.isnull(row['ListingDate']):
                listing_date = row['ListingDate'].strftime('%Y-%m-%d')

            data = {"name": row['Name'], "code": row['Symbol'], "exchange": row['Market'], "product": row['Industry'],
                    "listed_date": listing_date}
            model = set_stock_model(data)
            save_stock_company_info(model)

    def save_stock_to_company(self):
        result = get_stock_company_all()
        error_stock = []
        for data in result:
            print(data)
            start = None
            if data.listed_date is not None:
                start = datetime.strptime(data.listed_date, "%Y-%m-%d").date()

            code = data.code

            stock_data = get_stock(code, start, None)
            if stock_data is None:
                print((code, data.name))
                error_stock.append((code, data.name))
                continue

            stock_data['Date'] = stock_data.index
            stock_id = data.id

            for i, row in stock_data.iterrows():
                stock_price_model = set_stock_price_model({"Date": row['Date'].strftime('%Y-%m-%d'), "Open": row["Open"], "High": row['High'],
                                                           "Low": row["Low"], "Close": row["Close"],
                                                           "Volume": row["Volume"], "stock_id": stock_id})
                save_stock_company_info(stock_price_model)

        print("error_stock", error_stock)

    # 지정된 날짜 주식 검색, date가 None일 경우 오늘 날짜로 셋팅
    def save_stock_from_date(self, date=None):
        pass


if __name__ == '__main__':
    dc = DataController()
    # dc.save_stock_company_list()
    dc.save_stock_to_company()
    database_close()

