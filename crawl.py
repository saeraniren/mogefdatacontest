from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import pandas as pd

# 크롬 옵션 설정 (브라우저 안 뜨게 하고 싶으면 headless = True)
options = Options()
options.add_argument("--headless")  # headless 옵션 추가
options.add_argument("--disable-gpu")  # GPU 비활성화 (headless 모드에서 안정성 향상)
options.add_argument("--window-size=1920x1080") # 가상 브라우저 크기 설정
options.add_argument("--no-sandbox")  # (서버 환경에서 안정성 향상)
options.add_argument("--disable-dev-shm-usage")  # 메모리 이슈 방지 (Linux 환경용)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

# 드라이버 경로는 로컬 환경에 따라 수정
driver = webdriver.Chrome(options=options)

# 결과 저장 리스트
url_list = []

# selenium을 통한 검색 페이지 접속 및 링크 수집
for i in range(1, 41):
    url = f'https://section.cafe.naver.com/ca-fe/home/search/articles?q=아이돌봄서비스&t=1744266674263&p={i}'
    driver.get(url)
    time.sleep(1)  # JS 로딩 기다림

    # 불러와진 HTML을 BeautifulSoup으로 파싱
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    items = soup.select('div.item_list div.ArticleItem')

    print(f'페이지 {i} - 게시글 개수: {len(items)}')

    # 각 게시글의 링크를 추출하여 리스트에 저장
    for item in items:
        link_tag = item.select_one('a')
        if link_tag:
            link = link_tag.get('href')
            url_list.append(link)

# 저장된 링크 데이터 개수 출력
print(f'총 수집된 링크 수: {len(url_list)}')

def fetch_selenium(url, idx):
    try:
        driver.get(url)
        time.sleep(2) 

        # iframe 전환
        try:
            iframe = driver.find_element(By.CSS_SELECTOR, 'iframe#cafe_main')
            driver.switch_to.frame(iframe)
        except Exception as iframe_error:
            print(f"{idx}: iframe 없음 또는 전환 실패 → {iframe_error}")

        # iframe 내부의 HTML을 BeautifulSoup으로 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 제목과 본문 추출
        title_tag = soup.select_one('h3.title_text')
        content_tag = soup.select_one('div.se-main-container')
        reply_tag = soup.select_one('span.text_comment')

        title_text = title_tag.get_text(strip=True) if title_tag else '제목 없음'
        content_text = content_tag.get_text(strip=True) if content_tag else '내용 없음'
        reply_text = reply_tag.get_text(strip=True) if reply_tag else '댓글 없음'

        print(f'{idx}: 크롤링 완료 → {title_text}')
        return {'url': url, 'title': title_text, 'content': content_text, 'reply': reply_text}

    except Exception as e:
        print(f'{idx}번 페이지 에러: {e}')
        return None

results = []

# 비동기 실행 메인 함수
for idx, url in enumerate(url_list, start=1):
    data = fetch_selenium(url, idx)
    if data:
        results.append(data)
        
# 드라이버 종료
driver.quit()

# 결과를 DataFrame에 저장
df = pd.DataFrame(results)
print(df.head())

df.to_csv('crawled_data.csv', index=False, encoding='utf-8-sig')
print('크롤링 완료 및 CSV 파일 저장 완료')