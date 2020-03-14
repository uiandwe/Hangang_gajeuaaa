# -*- coding: utf-8 -*-
"""
한국 증권 거레소의 종목 가져오기
"""

import pandas as pd
# excel 파일을 다운로드하는거와 동시에 pandas에 load하기
# 흔히 사용하는 df라는 변수는 data frame을 의미합니다.
df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

# 상장일 기준 정렬
# df = df.sort_values(['상장일'], ascending=[True])

# 필요한 데이터만 추출
df = df[['회사명', '종목코드']]
df = df.rename(columns={'회사명': 'name', '종목코드': 'code'})
print(df.head())
