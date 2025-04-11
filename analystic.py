import os
import pandas as pd
import numpy as np
import crawl

# 데이터가 없을 경우 크롤링 실행
if not os.path.exists('data'):
    crawl.crawl_main()

# 데이터가 존재할 경우 CSV 파일을 읽어 DataFrame으로 변환
if os.path.exists('./data/crawled_data.csv'):
    # CSV 파일을 읽어 DataFrame으로 변환
    with open('./data/crawled_data.csv', 'r', encoding='utf-8') as f:
        contents = pd.read_csv(f)
