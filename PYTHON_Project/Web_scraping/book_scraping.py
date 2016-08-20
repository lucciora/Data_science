import requests
from bs4 import BeautifulSoup
import codecs


url= "http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf?orderClick=4da"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
book_list = soup.find_all(class_="detail")
f=codecs.open('yes24.txt',encoding='utf-8',mode='w')
count = 3
while count < 13:
    book_title = soup.find_all(class_="detail")[count].find(class_="title").text.strip()
    print(str(count-2)+"위 : "+book_title)
    f.write(str(count-2)+"위 : "+book_title+"\n")
    
    finding_author = soup.find_all(class_="detail")[count].find(class_="author").text.split("|")[0].strip()
    
    if len(finding_author)>10:
        book_author1 = soup.find_all(class_="detail")[count].find(class_="author").text.split("|")[0].split("저자 더보기")[0].strip()
        book_author2 = soup.find_all(class_="detail")[count].find(class_="author").text.split("|")[0].split("저자 더보기")[1].strip()
        print("\t"+book_author1+", "+book_author2)
        f.write("\n" + book_author1 + book_author2 + "\n")
    else:
        book_author = soup.find_all(class_="detail")[count].find(class_="author").text.split("|")[0].strip()
        print("\t"+book_author)
        f.write(book_author + "\n")
        
    book_publisher = soup.find_all(class_="detail")[count].find(class_="author").text.split("|")[1].strip()
    book_publish_date = soup.find_all(class_="detail")[count].find(class_="author").text.split("|")[2].strip()
    
    
    f.write(book_publisher + "\n")
    f.write(book_publish_date + "\n")
    
    
    print("\t"+book_publisher )
    print("\t"+book_publish_date)
    count+=1
    

f.close()

