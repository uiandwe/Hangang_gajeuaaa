# -*- coding: utf-8 -*-
"""
Subplot 기능을 활용하여 캔들차트와 보조지표(MACD) 출력하기

https://junpyopark.github.io/MACD_Plotting/


참고자료
http://blog.naver.com/anthouse28/221410326641
https://www.facebook.com/pg/TheAlphaSquare/photos/?tab=album&album_id=1229946413826362
"""
import pandas as pd
from datetime import datetime
from mpl_finance import candlestick2_ohlc
import matplotlib.pyplot as plt


# TODO 1단 그래프
# 캔들 그래프
# 바 그래프
# 선 그래프
# TODO 2단 그래프
# TODO 3단 그래프
class Graph:
    graph_types = ["line", "bar", "candle"]
    def __init__(self):
        pass

    def first_column(self, graph_data, y=[], type="line"):

        assert type in Graph.graph_types

        if type == "line":
            graph_data.plot(y=y, figsize=(20, 5))

        plt.show()

    def macd(self, df):
        pass


# import pandas as pd
# from domain.stock import Stock
# from datetime import datetime
#
# start = datetime(2020, 1, 1)
# end = datetime(2020, 3, 20)
# name = '삼성전자'
# stock = Stock()
# data = stock.get_stock(name, start, end)
#
# print(data.head())
# index = data.index.astype('str')
# print("Period from ", index[0], " To ", index[-1])
# print(list(data.columns.values))
# # 5일 이동평균선과 20일 이동평균선을 계산하여 저장합니다.
# ma5 = data['Close'].rolling(window=5).mean()
# ma20 = data['Close'].rolling(window=20).mean()


# https://www.facebook.com/pg/TheAlphaSquare/photos/?tab=album&album_id=1229946413826362
# MACD 계산 공식 참조

# Exponential Moving Average : 지수이동평균
# def EMA(close, timeperiod):
#     k = 2/(1+timeperiod) # k : smoothing constant
#     close = close.dropna()
#     ema = pd.Series(index=close.index)
#     ema[timeperiod-1] = close.iloc[0:timeperiod].sum() / timeperiod
#     for i in range(timeperiod,len(close)):
#         ema[i] = close[i]*k + ema[i-1] * (1-k)
#     return ema
#
# def MACD(close, fastperiod=12, slowperiod=26, signalperiod=9):
#     macd = EMA(close, fastperiod) - EMA(close, slowperiod)
#     macd_signal = EMA(macd, signalperiod)
#     macd_osc = macd - macd_signal
#     df = pd.concat([macd, macd_signal, macd_osc],axis=1)
#     df.columns = ['MACD', 'Signal', 'Oscillator']
#     return df
#
# close_price = data['Close'].astype(float)
# macd = MACD(close_price)
# print(macd.tail())


# import matplotlib.pyplot as plt
#
# plt.close('all')
# fig = plt.figure(figsize=(9,9))
#
# ax1 = plt.subplot2grid((3, 3), (0, 0))
# ax2 = plt.subplot2grid((3, 3), (0, 1), colspan=2)
# ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=2)
# ax4 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
#
# plt.tight_layout()
# plt.show()


# from mpl_finance import candlestick2_ohlc
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
#
# # 차트 레이아웃을 설정합니다.
# fig = plt.figure(figsize=(12,10))
# ax_main = plt.subplot2grid((5, 1), (0, 0), rowspan=3)
# ax_sub = plt.subplot2grid((5, 1), (3, 0))
# ax_sub2 = plt.subplot2grid((5, 1), (4, 0))
#
# # 메인차트를 그립니다.
# ax_main.set_title('Apple Inc. Q1~Q3 2018 Stock Price',fontsize=20)
# ax_main.plot(index, ma5, label='MA5')
# ax_main.plot(index, ma20, label='MA20')
# candlestick2_ohlc(ax_main,data['Open'],data['High'],data['Low'],data['Close'], width=0.6)
#
# ax_main.legend(loc=5)
#
# # 아래는 날짜 인덱싱을 위한 함수 입니다.
# def mydate(x,pos):
#     try:
#         return index[int(x-0.5)]
#     except IndexError:
#         return ''
#
# # ax_sub 에 MACD 지표를 출력합니다.
# ax_sub.set_title('MACD',fontsize=15)
# macd['MACD'].iloc[0] = 0
# ax_sub.plot(index,macd['MACD'], label='MACD')
# ax_sub.plot(index,macd['Signal'], label='MACD Signal')
# ax_sub.legend(loc=2)
#
# # ax_sub2 에 MACD 오실레이터를 bar 차트로 출력합니다.
# ax_sub2.set_title('MACD Oscillator',fontsize=15)
# oscillator = macd['Oscillator']
# oscillator.iloc[0] = 1e-16
# ax_sub2.bar(list(index), list(oscillator.where(oscillator > 0)), 0.7)
# ax_sub2.bar(list(index), list(oscillator.where(oscillator < 0)), 0.7)
#
# # x 축을 조정합니다.
# ax_main.xaxis.set_major_locator(ticker.MaxNLocator(7))
# ax_main.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
# ax_sub.xaxis.set_major_locator(ticker.MaxNLocator(7))
# ax_sub2.xaxis.set_major_locator(ticker.MaxNLocator(7))
# fig.autofmt_xdate()
#
# # 차트끼리 충돌을 방지합니다.
# plt.tight_layout()
# plt.show()
#
