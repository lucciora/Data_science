import requests
from bs4 import BeautifulSoup


url = "http://www.yes24.com/24/category/bestseller"

r= requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

count = 0
while count<10:
    
    html = soup.find(id="location_"+str(count))
    book_title = str(html).split('"')[7]
    
    print(count+1,"위 : " +book_title)
    count+=1
    