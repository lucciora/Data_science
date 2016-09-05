from selenium import webdriver
import time
from random import randint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup


def init_driver():
    driver = webdriver.Chrome("C:/Users/super/git/Data_science/chromedriver.exe")
    driver.wait = WebDriverWait(driver, 8)
    return driver

def login(driver, id, pw):
    driver.get("http://naver.com")
    sele = driver.find_element_by_id("id")
    sele.send_keys(id)
    sele=driver.find_element_by_id("pw")
    sele.send_keys(pw)
    sele.submit()
    time.sleep(randint(5,12))
    
def init_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup
    

def lookup(driver):
    
    week=['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for weekday_ in week:
        driver.get("http://comic.naver.com/webtoon/weekdayList.nhn?week="+weekday_)
        url="http://comic.naver.com/webtoon/weekdayList.nhn?week="+weekday_
        soup = init_soup(url)
        number_webtoon = len(soup.find_all("div", {"class":"thumb"}))
        print(number_webtoon)
        for number in range(3, number_webtoon-3):
            numbering = number-2
            title = soup.find_all("div", {"class":"thumb"})[number].find('a').get('title')
            time.sleep(randint(8,14))
            genre = " "
            storywriter = soup.find_all("dd", {"class":"desc"})[number].find('a').text
            illustrator = " "
            platform = "네이버"
            time.sleep(randint(8,14)) 
            startdate= "00000000"
            address = "http://comic.naver.com/" + soup.find_all("div", {"class":"thumb"})[number].find('a').get('href')
            weekday = weekday_
            time.sleep(randint(8,14)) 
            image = soup.find_all("div", {"class":"thumb"})[number].find('img').get('src')
            print(numbering, title, genre, storywriter, illustrator, platform, startdate, address, weekday, image)
            
        
            
       
        
    
    
    
           
if __name__ == "__main__":
    driver = init_driver()
    id = input("아이디")
    pw = input("비밀번호")
    login(driver, id, pw)
    time.sleep(randint(4,10))
    lookup(driver)
    
        
        
        
        
        
        
        