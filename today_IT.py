import requests
from bs4 import BeautifulSoup as bs

url = "https://news.daum.net/digital#1"

r = requests.get(url)

soup = bs(r.text, "html.parser")

boxes_list = soup.select("ul[class=list_newsmajor] > li")

chit = dict()
for box in boxes_list:
    link = box.select("a[class=link_txt]")[0].attrs['href']

    ungung = requests.get(link)

    ung = bs(ungung.text, "html.parser")
    ung_tit = ung.select("h3[class=tit_view]")[0]
    title = ung_tit.text
    ung_nae = ung.select("div[class=news_view]")[0]
    naeyong = ung_nae.text

    chit.update({title:naeyong})

with open("today_IT.txt", "w", encoding="UTF-8") as f:
    for k,v in chit.items():
        f.write(k+v)