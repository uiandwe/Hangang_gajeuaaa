# -*- coding: utf-8 -*-
import pandas as pd
import pandas_datareader as pdr
import datetime
from matplotlib import pyplot as plt


class Stock:
    stock_type = {
        'kospi': 'stockMkt',
        'kosdaq': 'kosdaqMkt'
    }

    def get_stock(self, name='', start=None, end=None):
        kospi_df = self.get_stock_code_kospi()
        kosdaq_df = self.get_stock_code_kosdaq()
        # data frame merge
        code_df = pd.concat([kospi_df, kosdaq_df])
        # data frame정리
        code_df = code_df[['회사명', '종목코드']]
        # data frame title 변경 '회사명' = name, 종목코드 = 'code'
        code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
        code = self.get_code(code_df, name)
        print(code)
        # 수정주가를 반영
        df = pdr.get_data_yahoo(code, start, end, adjust_price=True)
        return df

    def get_code(self, df, name):
        # 회사명으로 주식 종목 코드를 획득할 수 있도록 하는 함수
        code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
        # 위와같이 code명을 가져오면 앞에 공백이 붙어있는 상황이 발생하여 앞뒤로 sript() 하여 공백 제거
        code = code.strip()
        return code

    def get_stock_code(self, market_type=None):
        # download url 조합
        market_type_param = Stock.stock_type[market_type]
        download_link = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
        download_link = download_link + '?method=download'
        download_link = download_link + '&marketType=' + market_type_param
        df = pd.read_html(download_link, header=0)[0]
        return df

    def get_stock_code_kospi(self):
        # kospi 종목코드 목록 다운로드
        df = self.get_stock_code('kospi')
        df.종목코드 = df.종목코드.map('{:06d}.KS'.format)
        return df

    def get_stock_code_kosdaq(self):
        # kosdaq 종목코드 목록 다운로드
        df = self.get_stock_code('kosdaq')
        df.종목코드 = df.종목코드.map('{:06d}.KQ'.format)
        return df

if __name__ == '__main__':
    start = datetime.datetime(2015, 1, 1)
    end = datetime.date(2019, 12, 31)
    name = '삼성전자'

    stock = Stock()
    df = stock.get_stock(name, start, end)
    df.plot()
    plt.show()
