# 네이버 블로그를 crawling 하여 원하는 내용을 추출하고 분석하는 코드.

import re
import requests
import urllib.request
from bs4 import BeautifulSoup
from konlpy.tag import Twitter  # 한국어 명사를 분리 및 추출하기 위한 위한 pkg
from collections import Counter  # 키워드의 빈도수 계산을 위한 딕셔너리형 객체 명사만을 분리하기 위해 사용


# 주소창에서 복사한 url은 HTML 소스코드를 가지고 있지 않고, 연결의 역할만 하기 때문에
# HTML 소스를 가지고 있는 오리지널(origin) URL로 바꿔주는 작업을 해야한다.
def get_origin_url(url):
    html_result = requests.get(url)  # HTML 소스코드 가져오기
    soup_temp = BeautifulSoup(html_result.text, 'lxml')  # 소스코드 파싱 (parser보다 lxml이 보다 빠르다하여 사용)
    area_temp = soup_temp.find(id='mainFrame')  # Id가 mainFrame인 frame 태그 서치
    url_2 = area_temp.get('src')  # mainFrame의 origin 주소 일부 추출
    origin_url = "http://blog.naver.com" + url_2  # 추출해낸 주소를 접속할 수 있도록 결합
    return origin_url


# 블로그의 제목과 본문 추출하기
def get_text(url):
    origin_url = get_origin_url(url)  # 블로그를 crawling 하기위한 origin url 변환
    result = ""  # 추출한 내용을 저장하기 위한 string 생성

    # 제목과 본문부분 추출하기
    res = urllib.request.urlopen(origin_url)
    soup = BeautifulSoup(res, 'lxml')  # html.parser보다 처리속도가 월등히 빠름.

    # title 추출하기
    # 크롬 검사기능을 활용하여 태그 위치정보 사용.
    title = soup.findAll("span", {"class": "pcol1 itemSubjectBoldfont"})
    for t in title:
        text = no_space(t.get_text())  # title의 html 코드 출력 (즉,제목 text)
        #print(text)  # 확인용.
        result += text  # 파일 저장을 위한 DATA 취합

    # 본문 추출하기
    body = soup.findAll("div", {"id": "postViewArea"})
    for b in body:
        text = no_space(b.get_text())   # body의 html 코드 출력 (즉,본문내용 text)
        # print(text)  # 확인용.
        result += text  # title 과 body 같이 저장.
        # 한 줄씩 출력하려면 어떻게 해야할까....?

    # 다른 기능에서 활용을 위해, 파일로 저장. 인코딩 필수!
    f = open('body.txt', 'w', encoding='utf-8')
    f.write(result)
    f.close()

    return result


# 텍스트에서 명사를 분리/추출한 후, 빈도 계산하기
def get_tags(text, number=50):  # text: 분석할 내용, number: 빈도수 상위 50개(defalut)
    splitter = Twitter()  # konlpy의 Twitter 객체사용
    nouns = splitter.nouns(text)  # nouns 함수를 통해서 text 에서 명사만 분리/추출
    count = Counter(nouns)  # Counter 객체를 생성하고 참조변수 nouns 할당
    cnouns_list = []  # 명사 빈도수 저장할 변수

    for n, c in count.most_common(number):  #n: 명사, c:빈도수
        ncdict = {'tag': n, 'count': c}
        cnouns_list.append(ncdict)
        # most_common 메소드는 정수를 입력받아, 객체 안의 명사중 빈도수가 큰 명사부터
        # 순서대로 입력받은 정수 갯수만큼 저장되어있는 객체 반환
        # 명사와 빈도수를 cnouns_list 에 저장합니다.
    return cnouns_list
    # [{'tags': '명사1', 'count': N1}, {'tags': '명사2', 'count': N2}, ... ,{'tags': '명사50', 'count': N50}]


# 추출한 본문내용으로 명사/빈도수 딕셔너리 파일에 저장하기
def save_tags(url):  # main에서 받아오는 url
    text = get_text(url)  # 해당 url의 text 즉, 본문내용 추출하여 가져오기.
    noun_count = 50  # 빈도수 상위 50개(defalut)
    tags = get_tags(text, noun_count) # 본문내용에서 명사 분석
    f = open("cnouns_list.txt", 'w', encoding='utf-8') # 후에 다른 함수에서 원활한 가공을 위해 파일로 저장. 한글이기 때문에 인코딩 필수
    # 원하는 포맷으로 순차적으로 분석결과 저장.
    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        f.write('{} {}\n'.format(noun, count))
        # if len(noun > 2) 로 한 글자인 경우를 삭제하려 하였으나, 실패
        #명사1, N1
        #명사2, N2
        #명사3, N3
        #.
        #.
        #.
        #명사50, N50
    f.close()


# 추출한 내용에 불필요한 특수기호 삭제하기
# 중간에 필요해서 구현했지만, 현재는 필요가 없다. 만일을 위해 남김.
def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)
    return cleaned_text


# 내용과 무관한 공백, 연속적인 엔터 삭제
def no_space(text):
    cleaned_text = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', text)
    cleaned_text = re.sub('\n\n', '', cleaned_text)
    return cleaned_text


