# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime


class DataController:

    def __init__(self, get_stock_company_from_name=None, get_korea_stock_list=None, set_stock_model=None,
                 database_close=None, get_stock_company_all=None, get_stock=None, set_stock_price_model=None):
        self.get_stock_company_from_name = get_stock_company_from_name
        self.get_korea_stock_list = get_korea_stock_list
        self.set_stock_model = set_stock_model
        self.database_close = database_close
        self.get_stock_company_all = get_stock_company_all
        self.get_stock = get_stock
        self.set_stock_price_model = set_stock_price_model


    def save_stock_company_list(self):
        stock_company_list = self.get_korea_stock_list()

        for i, row in stock_company_list.iterrows():
            listing_date = None
            if not pd.isnull(row['ListingDate']):
                listing_date = row['ListingDate'].strftime('%Y-%m-%d')

            data = {"name": row['Name'], "code": row['Symbol'], "exchange": row['Market'], "product": row['Industry'],
                    "listed_date": listing_date}
            model = self.set_stock_model(data)
            self.save_stock_company_info(model)
        self.database_close()

    def save_stock_to_company(self):
        # 전체 데이터 검색에 따른 가용시간으로 일단 폐기
        return None

        result = self.get_stock_company_all()
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
        self.database_close()
        print("error_stock", error_stock)

    def get_company_name_code(self, company_name, start=None, end=None):
        row_data = self.get_stock_company_from_name(company_name)

        df = self.get_stock(row_data[0].code, start, end)

        return df
