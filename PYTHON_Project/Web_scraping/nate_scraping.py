import requests
from bs4 import BeautifulSoup
import csv

csvfile = open("nate.csv", "w", encoding ="utf-8", newline = '')
writer = csv.writer(csvfile, delimiter=',')
writer.writerow(['title', 'genre', 'storywriter', 
                         'illustrator', 'platform', 
                         'startdate', 'address'])


url = "http://comics.nate.com/webtoon/?category=2"
r= requests.get(url)
soup = BeautifulSoup(r.text, "html.parser", from_encoding="UTF-8")
webtoons = soup.find_all('a', {'class' : 'wtl_toon'})
print(len(webtoons))

for i in range(len(webtoons)):
    title = str(webtoons[i].find('span', {'class' : 'wtl_title'}).text)
    genre = "comic"
    storywriter = webtoons[i].find('span', {'class' : 'wtl_author'}).text
    illustrator = "xxx"
    platform = "네이트"
    startdate = "20000101"
    address = "http://comics.nate.com/"  + webtoons[i].get('href')
    writer.writerow([title, genre, storywriter,
                         illustrator, platform,
                         startdate, address])
   



# write_csv(title, genre, strorywriter,illustrator, platform, startdate, address)
