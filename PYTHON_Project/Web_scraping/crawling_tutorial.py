import requests
from bs4 import BeautifulSoup
#python으로 web crawling 하기 to jelly

# 크롤링하고 싶은 주소, 여기서는 교보문고 베스트 셀러를 선택
url = "http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf?orderClick=4da"

# requests 패키지를 통해 url 내용을 얻어옮
r = requests.get(url)

# html 문서의 내용을 text로 변환
soup= BeautifulSoup(r.text, "html.parser")

# 문장에서 첫번째 a 태그의 href 속성값을 뽑아냄
first_a = soup.find('a').get('href')
print(first_a)

# 첫 번째 p의 텍스트를 뽑아냄 <p>텍스트</p>
first_p = soup.find('p').text
print(first_p)

# 모든 a 태그들을 뽑아서 리스트에 저장
all_a = soup.find_all('a')
print(all_a)

# 특정 클래스를 가진 태그 뽑아내기
certain_class = soup('p', {'class' : 'path'})
print(certain_class)

# 태그 안에 있는 태그 뽑기, ResultSet이기 때문에 [0]을 붙여줘야 함
tag_in_tag = soup.find_all('ul', {'class' : 'link_list'})[0].find('li').text
print(tag_in_tag)
                                  



