# -*- coding: utf-8 -*-
"""
Stochastic 차트 그리기

https://excelsior-cjh.tistory.com/111?category=975542

Stochastic은 주식분석에서 MACD와 같이 기술적 분석에 사용되는 보조지표로써, 공식 명칭은 Stochastic Oscillator이다. Stochastic은 1950년대
William Dunnigun이 고안하고 George Lane이 널리 보급하였다고 한다.(출처: Wikipedia) Stochastic은 현재주가가 일정 기간의 주가 변동폭 중 어디에
위치하는지를 백분율 로 나타낸 지표이다.

Stochastic은 최근 N일 간의 최고가와 최저가의 범위 내에서 현재 가격의 위치를 표시할 때 매수세가 매도세 보다 강할 때는 그 위치가 높게 형성되고,
매도세가 매수세 보다 강할 떄는 그 위치가 낮게 형성된다는 것을 이용한 것이다.
예를 들어, 최근 5일간 최고가가 15,000원이고 최저가가 10,000원인 주식이 있을때, 현재가가 14,000원이라면 매수세가 강하여 오르는 추세임을 알 수 있다.
만일 현재가가 11,000원이라면 매도세가 강하여 내리는 추세임을 알 수 있다.



"""
from factory import get_company_from_name_to_data


# 일자(n,m,t)에 따른 Stochastic(KDJ)의 값을 구하기 위해 함수형태로 만듬
def get_stochastic(df, n=15, m=5, t=3):
    # n일중 최고가
    ndays_high = df.High.rolling(window=n, min_periods=1).max()
    # n일중 최저가
    ndays_low = df.Low.rolling(window=n, min_periods=1).min()

    # Fast%K 계산
    kdj_k = ((df.Close - ndays_low) / (ndays_high - ndays_low)) * 100
    # Fast%D (=Slow%K) 계산
    kdj_d = kdj_k.ewm(span=m).mean()
    # Slow%D 계산
    kdj_j = kdj_d.ewm(span=t).mean()

    # dataframe에 컬럼 추가
    df = df.assign(kdj_k=kdj_k, kdj_d=kdj_d, kdj_j=kdj_j).dropna()

    return df


if __name__ == '__main__':

    df = get_company_from_name_to_data("삼성전자", '2020')

    df = get_stochastic(df)
    print(df.head())

    index = df.index.astype('str')

    from mpl_finance import candlestick2_ohlc
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    # 차트 레이아웃을 설정합니다.
    fig = plt.figure(figsize=(12,10))
    ax_main = plt.subplot2grid((5, 1), (0, 0), rowspan=3)
    ax_sub = plt.subplot2grid((5, 1), (3, 0))
    ax_sub2 = plt.subplot2grid((5, 1), (4, 0))

    # 메인차트를 그립니다.
    ax_main.set_title('',fontsize=20)
    ax_main.plot(index, df['kdj_d'], label='Slow%K')
    ax_main.plot(index, df['kdj_j'], label='Slow%D')
    ax_main.legend(loc=5)

    ax_sub.set_title('Volume', fontsize=15)
    ax_sub.bar(index, df['Volume'], label='Volume')
    ax_sub.legend(loc=2)

    # 차트끼리 충돌을 방지합니다.
    plt.tight_layout()
    plt.show()

