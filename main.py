# -*- coding: utf-8 -*-
from factory import get_company_from_name_to_data, valid_date, get_graph_first_column
from matplotlib import pyplot as plt



if __name__ == '__main__':
    start = "2018"
    start = "201812"
    start = "20181231"
    start = "2020"

    start = valid_date(start)

    df = get_company_from_name_to_data("GS홈쇼핑", start)

    # df['Close'].plot()

    #line
    # get_graph_first_column(df, ['Close'])
    #bar
    # get_graph_first_column(df, ['Close'], 'bar')
    #candle
    get_graph_first_column(df, [], 'candle')
    plt.show()
