import requests
from bs4 import BeautifulSoup

url = "http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf?orderClick=4da"

r =requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
'''
title = soup.find_all("div", {'class':'title'})[5].find('a').text
name = soup.find(class_="author").text.split("|")[2].strip()

print(title + ' ' + name)

'''
for i in range(2, 14):
    title = soup.find_all("div", {'class':'title'})[i+2].find('a').text
    name = soup.find_all(class_="detail")[i].find(class_="author").text.split("|")[0].strip()
    print(title + " " + name)