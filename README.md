<img src="https://honored-nigella-fc0.notion.site/image/attachment%3Ae7712f5f-3410-40b7-81ff-40fc968e3544%3AWhite_and_Grey_Modern_Business_Research_Proposal_Presentation.png?table=block&id=1f2e008e-cc3a-80b9-bba1-ca685255ae88&spaceId=941bde33-6d61-4dec-a0a5-5165a3ad9646&width=1420&userId=&cache=v2">

# 🚀 사회 경제적 지표 기반 지역별 아이돌보미 수요 예측 시나리오 분석

- 프로젝트명 : 사회 경제적 지표 기반 지역별 아이돌보미 수요 예측 시나리오 분석
- 진행 기간 : 2025년 4월 3일 ~ 2025년 5월 9일
- 프로젝트 활용 목적 : 아이돌봄 서비스 정책 제언
- 활용 기술
    - 언어 : Python
    - 데이터 시각화 : Matplotlib, Seaborn
    - 머신러닝 : Scikit-learn(Lasso, Ridge, ElasticNet, RandomForest, TF-IDF), XGBoost
    - 데이터 수집 : Selenium, BeautifulSoup
    - 외부 활용 기술 : Gephi
    - 팀 협업 방식 : GitHub 형상 관리, Notion으로 분석 과정 기록 및 회의 진행
- [PPT 바로가기](https://www.canva.com/design/DAGklaJa1ss/x-Z0JlExcqf_rVpjzKYn-w/view?utm_content=DAGklaJa1ss&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h151e16bd3a)

# ❓ 프로젝트 개요

2025년 현재, 우리나라의 합계출산율은 0.75로 세계 최저 수준을 기록하고 있으며, 이로 인해 인구 구조의 불균형과 노동력 감소 등 다양한 사회적 문제가 우려되고 있다. 이에 따라 정부는 양육 부담을 덜고, 공백을 해소하 위한 방안으로 ‘아이돌봄’ 서비스를 점차 확대해오고 있다.

하지만, 공급이 수요를 따라가지 못해 긴 대기 시간이 발생하는 등 운영상 한계도 나타나고 있다. 이에 단순 신청 건수 중심의 접근이 아닌, 지역별 사회경제적 특성과 수요의 세부적인 양상을 함께 고려하여 보다 효과적인 서비스 개선 방안을 모색하고자 분석을 진행하였다.

# 💽 데이터 소개

| 출처 | 데이터명 | 사용 컬럼 또는 설명 |
| --- | --- | --- |
| 자체설문조사 | 아이돌봄서비스 인식 및 수요조사 | 서비스 인지도, 이용 경험, 수요 및 의향, 개선사항 |
| 행정안전부 | 주민등록인구 및 세대현황(년) | 행정구역, 0세~12세 인구 수 |
| 교육부 | 어린이집 및 이용자 통계(2023) | 지역별 어린이집 미설치 지역, 어린이집 정원, 어린이집 현원, 직장어린이집 수 |
| 통계청 | 인구총조사 (2023) | 행정구역, 총가구 수, 총가구원 수 |
|  | 지역소득 (2023) | 시도별 지역 내 총생산 (명목) |
|  | 인구동향조사 (2022) | 출생아수(명) |
|  | 육아휴직통계 (2023) | 광역별, 육아휴직 사용한 부모 수 |
| 여성가족부 | 가족실태조사 (가족돌봄) (2023) | 자녀돌봄 서비스가 가장 필요한 평일 시간대 |
| 여성가족부 (공공데이터포털) | 아이돌봄 월별신청현황 - 시간대별 | 연도, 기관명, 돌봄구분, 총신청건수, 시간대별 신청건수 |
|  | 아이돌봄 월별신청현황 - 연령대별 | 연도, 기관명, 연령별(0~12세) 신청건수 |
|  | 아이돌봄 누적아동실적현황 - 연령별 | 연도, 기관명, 연령별(0~12세) 아동 수 |
|  | 아이돌보미 현황 정보 | 연도, 기관명, 당월 및 누적 돌보미 수 (자격증 여부 포함) |
|  | 아이돌보미 현황 - 성별 | 연도, 기관명, 남성/여성 돌보미 수 |
|  | 아이돌보미 현황 - 연령대별 | 연도, 기관명, 연령대별(40세 ~ 65세) 돌보미 수 |
|  | 아이돌보미 교육기관 | 연도, 교육기관명 |

# 👤프로젝트에서 진행한 역할

- ‘아이돌봄 서비스’ 관련 온라인 커뮤니티 게시글 데이터 수집
- NLP 방식 불용어 텍스트 전처리
- 게시물 내용을 바탕으로 워드클라우드 시각화 및 의미 연결망 시각화

# ⚙️ 문제 설정

🔔**“우리가 항상 뉴스로 보던 내용들이 과연 온라인 커뮤니티에서도 똑같이 이야기를 할까?”**

뉴스나 정책에서 다루는 이슈와 실제 온라인 커뮤니티에서 이용자들이 나누는 대화 사이에는 간극이 존재할 수 있다. 온라인 커뮤니티는 자발적이고 솔직한 의견이 모이는 공간이므로, 이를 텍스트 분석해 주요 키워드와 주제를 도출함으로써 사회적 담론과 실제 경험 간 차이를 확인하고, 서비스 현장의 진짜 문제와 이용자들이 체감하는 불편을 파악하여 정책 개선과 품질 향상을 위한 **핵심 키워드**를 찾고자 하였다.

# 🚈 분석 과정

## 데이터 수집

```python
# selenium을 통한 검색 페이지 접속 및 링크 수집
for search_name in ['아이돌봄서비스', '맘시터', '하이시터', '시터넷', '세이프시터', '시터']:
    # 현재 검색어 출력
    print(f'검색어: {search_name}')

    for i in range(1, 41):
        url = f'https://section.cafe.naver.com/ca-fe/home/search/articles?q={search_name}&t=1744266674263&p={i}'
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
```

- Selenium을 사용해, 네이버 카페의 검색 기능을 활용하여 ‘아이돌봄서비스, 맘시터, 하이시터, 시터넷, 세이프시터’ 등 관련 키워드 기반의 게시글 데이터를 수집하였다. 검색 페이지를 자동으로 탐색하고, 각 게시글의 링크/제목/본문/댓글을 추출하였다.

```python
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
```

- 이 과정에서 iframe 전환, 페이지 로딩 지연 처리, user-agent설정 등 안정적인 크롤링을 위한 예외 처리를 적용하였다.

```python
# 결과를 DataFrame에 저장
df = pd.DataFrame(results)
print(df.head())

df.to_csv('crawled_data.csv', index=False, encoding='utf-8-sig')
print('크롤링 완료 및 CSV 파일 저장 완료')
```

- 이렇게 모인 데이터를 DataFrame으로 변환하여 csv로 원천 데이터로써 저장하였다.

## 데이터 전처리

### 형태소 분석 및 전처리

```python
# 형태소 분석
okt = Okt()
nouns = okt.nouns(text)
```

- 수집된 텍스트에 대해 **KoNLPy의 Okt 형태소 분석기**를 사용하여 **명사만 추출**

```python
# 자동 불용어 추출 (상위 top_k_auto 중 의미 약한 단어 제거)
common_words = [word for word, _ in word_count.most_common(top_k_auto)]
```

- 1~2글자 단어 및 빈도 기반 자동 불용어 추가 필터링 수행

```python
# 최종 불용어 세트
stopwords = base_stopwords.union(set(common_words) if auto_stopword else set())
```

- 의미 없는 단어를 제거하기 위해 **불용어 리스트를 적용**

### TF-IDF 가중치 계산

```python
# TF-IDF
tfidf_vectorizer = TfidfVectorizer(analyzer='word',
                                   lowercase=False,
                                   tokenizer=None,
                                   preprocessor=None,
                                   min_df=5,
                                   ngram_range=(1, 2), # 한국어
                                   smooth_idf=True,
                                   max_features=1000)

# TF-IDF 훈련
tfidf_vector = tfidf_vectorizer.fit_transform(contents['tokens'].astype(str))

# 결과 확인
print(tfidf_vector)
```

- 문서별로 단어의 중요도를 측정하기 위해 **TF-IDF**방식을 적용
- 이를 통해 **문서 내에서는 자주 등장하지만 전체 문서에서는 희귀한 단어**를 상대적으로 중요한 키워드로 판단

### 유사도 기반 네트워크 구성

```python
# 엣지 리스트 만들기 (유사도가 높은 쌍만)
threshold = 0.2  # 유사도 임계값
edges = []

for i in range(len(term_term_mat)):
    for j in range(i+1, len(term_term_mat)):
        sim = term_term_mat.iloc[i, j]
        if sim > threshold:
            source = term_term_mat.index[i]
            target = term_term_mat.columns[j]
            edges.append((source, target, sim))

# 엣지 DataFrame
edges_df = pd.DataFrame(edges, columns=['Source', 'Target', 'Weight'])
edges_df.to_csv("term_edges.csv", index=False)
```

- TF-IDF 행렬을 바탕으로 각 단어 간 **Cosine Similarity**를 계산하여 **Term-Term 유사도 행렬** 생성
- 유사도가 높은 단어쌍을 연결하여 **키워드 관계 네트워크** 구성

## 네트워크 시각화 (Gephi 활용)

- 유사도 기반으로 생성된 키워드 네트워크를 **Gephi**를 활용하여 시각화
- *곡선 엣지(Curved Edges)**를 적용하여 노드 간 관계를 명확하게 표현
- **Modularity 알고리즘**을 사용해 키워드 클러스터를 구분하고, **Degree Centrality**를 통해 중심 키워드를 도출

# ❕ 분석 결과

<img src="https://honored-nigella-fc0.notion.site/image/attachment%3A9477b382-89f9-4da1-9f31-bf7283f204a7%3Aimage.png?table=block&id=267e008e-cc3a-80b9-abb4-c1136a62a34c&spaceId=941bde33-6d61-4dec-a0a5-5165a3ad9646&width=1420&userId=&cache=v2">

- “서류, 자격, 시간제, 기준, 비용”과 같은 키워드들이 빈번하게 나타난 것으로 보아 **아이돌봄서비스 신청 절차와 유형 관련 글이 많은 것을 파악.**

<img src="https://honored-nigella-fc0.notion.site/image/attachment%3Aad5640d7-4342-46c1-8632-797f67a043fb%3Aimage.png?table=block&id=267e008e-cc3a-80c1-a93b-c1d6521f18fd&spaceId=941bde33-6d61-4dec-a0a5-5165a3ad9646&width=1420&userId=&cache=v2">

- 맞벌이 또는 복직을 앞둔 가구의 아이돌봄서비스에 대한 수요 뿐만 아니라, **아이돌보미 자격 요건 및 채용공고에 대한 관심이 있음을 확인.**

# 💡 프로젝트 내 회고

- 이번 공모전 프로젝트를 통해 처음으로 텍스트 마이닝 기법을 활용한 데이터 전처리와 분석 과정을 경험하게 되었다. 이를 통해 텍스트 마이닝 기법 전반에 대한 실질적인 경험을 쌓을 수 있었다.
- KoNLPy를 활용한 형태소 분석으로 텍스트 데이터를 정제·전처리 한 뒤, TF-IDF를 통해 단어의 중요도를 수치화하고 분석에 활용하는 과정은 매우 흥미로웠다. 단순히 자주 등장하는 단어를 보는 데 그치지 않고, 문서 내에서 상대적인 중요도를 반영해 보다 행심적인 키워드를 도출할 수 있었던 점이 인상깊었다.
- 도출된 단어들 간의 유사도를 기반으로 의미 연결망을 구성하고 Gephi로 시각화하는 과정에서, 정성적 데이터 속에서도 구조적인 인사이트를 도출할 수 있다는 가능성을 체감할 수 있었다.
- 텍스트 데이터를 활용한 EDA의 새로운 접근 방식을 배운 프로젝트였으며, 앞으로 다양한 분석 프로젝트에 이러한 기법을 적용해보고 싶다는 동기를 얻게 되었다.
