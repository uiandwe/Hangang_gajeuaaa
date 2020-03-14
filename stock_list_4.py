# -*- coding: utf-8 -*-
"""
주식 정보 이동 평균
https://wendys.tistory.com/178?category=769564
"""

import pandas as pd
import pandas_datareader as pdr
import datetime
import numpy as np

from matplotlib import pyplot as plt
# 종목 타입에 따라 download url이 다름. 종목코드 뒤에 .KS .KQ등이 입력되어야해서 Download Link 구분 필요
stock_type = {
'kospi': 'stockMkt',
'kosdaq': 'kosdaqMkt'
}
# 회사명으로 주식 종목 코드를 획득할 수 있도록 하는 함수
def get_code(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)
    # 위와같이 code명을 가져오면 앞에 공백이 붙어있는 상황이 발생하여 앞뒤로 sript() 하여 공백 제거
    code = code.strip()
    return code
# download url 조합
def get_stock_code(market_type=None):
    market_type_param = stock_type[market_type]
    download_link = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
    download_link = download_link + '?method=download'
    download_link = download_link + '&marketType=' + market_type_param
    df = pd.read_html(download_link, header=0)[0]
    return df
# kospi 종목코드 목록 다운로드
def get_stock_code_kospi():
    df = get_stock_code('kospi')
    df.종목코드 = df.종목코드.map('{:06d}.KS'.format)
    return df
# kosdaq 종목코드 목록 다운로드
def get_stock_code_kosdaq():
    df = get_stock_code('kosdaq')
    df.종목코드 = df.종목코드.map('{:06d}.KQ'.format)
    return df
# Fast %K = ((현재가 - n기간 중 최저가) / (n기간 중 최고가 - n기간 중 최저가)) * 100
def get_stochastic_fast_k(close_price, low, high, n=5):
    fast_k = ((close_price - low.rolling(n).min()) / (high.rolling(n).max() - low.rolling(n).min())) * 100
    return fast_k
# Slow %K = Fast %K의 m기간 이동평균(SMA)
def get_stochastic_slow_k(fast_k, n=3):
    slow_k = fast_k.rolling(n).mean()
    return slow_k
# Slow %D = Slow %K의 t기간 이동평균(SMA)
def get_stochastic_slow_d(slow_k, n=3):
    slow_d = slow_k.rolling(n).mean()
    return slow_d
# kospi, kosdaq 종목코드 각각 다운로드
kospi_df = get_stock_code_kospi()
kosdaq_df = get_stock_code_kosdaq()
# data frame merge
code_df = pd.concat([kospi_df, kosdaq_df])
# data frame정리
code_df = code_df[['회사명', '종목코드']]
# data frame title 변경 '회사명' = name, 종목코드 = 'code'
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
code = get_code(code_df, '삼성전자')
start = datetime.datetime(2015,1,1)
end = datetime.date(2019,12,31)
# 수정주가를 반영
df = pdr.get_data_yahoo(code, start, end, adjust_price=True)

def weighted_mean(weight_array):
    def inner(x):
        return (weight_array * x).mean()
    return inner

weights = np.arange(1,6)
wma5 = df['Close'].rolling(5).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
weights = np.arange(1,21)
wma20 = df['Close'].rolling(20).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
weights = np.arange(1,101)
wma100 = df['Close'].rolling(100).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
weights = np.arange(1,201)
wma200 = df['Close'].rolling(200).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)

df1 = pd.DataFrame()
df1['wma5'] = wma5
df1['wma20'] = wma20
df1['wma100'] = wma100
df1['wma200'] = wma200

df1.plot()
plt.show()
