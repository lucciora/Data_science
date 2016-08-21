import requests
from bs4 import BeautifulSoup


url = "http://www.kyobobook.co.kr/newproduct/newTopicKorList.laf?mallGb=KOR"
r=requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")

#first_paragraph = soup.find('p')
#print(first_paragraph)

#first_paragraph_text = soup.a.text.strip()
#print(first_paragraph_text)

#first_dl = soup.dl['class']
#print(first_dl)

#all_divs = soup.find_all('dl')
#dls_with_ids = [p for p in soup('dl') if p.get('class')]
#print(dls_with_ids)

#important_dl = soup('dl', {'class':'book_title'})
#print(important_dl)

#미완성
'''
spans_inside_divs = [li
                     for dl in soup.find('dl')
                     for li in dl]

print(spans_inside_divs)
'''
