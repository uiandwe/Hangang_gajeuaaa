# -*- coding: utf-8 -*-
"""
네이버 금융 기사 수집
"""

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time
import datetime
import os
import re
from googletrans import Translator
translator = Translator()


def get_title_data(code): # 1년간의 기사 데이터 받아오기
    p = 0
    data = pd.DataFrame(columns=['title','Link','info'])

    while True:
        p = p + 1
        time.sleep(0.3 + np.random.rand())
        url = 'http://finance.naver.com/item/news_news.nhn?code={code}&page={page}&sm=title_entity_id.basic&clusterId='
        soup = BeautifulSoup(requests.get(url.format(code=code, page=p), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'}).text, 'lxml')
        alist = soup.select('tr')
        print('Page : ',p, '    Articles : ',len(alist))
        if len(alist) < 11 :
            break
        for tr in alist:
            try:
                href = 'http://finance.naver.com' + tr.select('a')[0]['href']
                title = tr.select('a')[0].text.strip()
                info = tr.select('.info')[0].text.strip()
                date = tr.select('.date')[0].text.strip()
                dt = datetime.datetime.strptime(date, "%Y.%m.%d %H:%M")
                data.loc[dt] = [title, href, info]
                # print(href, title, info, date)
            except IndexError as e:
                continue
    data.to_csv(code + '.csv')
    return data

def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', cleaned_text)
    return cleaned_text

if __name__ == '__main__':
    kakao_code = '035720'
    csv_kakao = kakao_code+'.csv'
    if not os.path.isfile(csv_kakao):
        get_title_data(kakao_code)
    kakao_article = pd.read_csv(csv_kakao, index_col=0)
    print(list(kakao_article.columns.values))

    en_title = kakao_article['title'].apply(lambda title: clean_text(title))
    kakao_article['en_title'] = en_title

    print(kakao_article.head())
