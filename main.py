# -*- coding: utf-8 -*-
from factory import get_company_from_name_to_data
from matplotlib import pyplot as plt

if __name__ == '__main__':
    df = get_company_from_name_to_data("GS홈쇼핑", '2018')

    df['Close'].plot()
    plt.show()
