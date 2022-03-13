import requests
from bs4 import BeautifulSoup as bs

url = "https://news.daum.net"

r = requests.get(url)

soup = bs(r.text, "html.parser")

news_list = soup.select("ul[class=list_newsissue] > li")

idk = dict()
for news in news_list:
    link = news.select("a[class=link_txt]")[0].attrs['href']

    r = requests.get(link)
    soup = bs(r.text, "html.parser")

    title = soup.select("h3[class=tit_view]")[0].text
    content = soup.select("div[class=article_view]")[0].text

    idk.update({title:content})

with open("jybabo.txt" ,"w",encoding="UTF-8") as f:
    for title, content in idk.items():
        f.write(f"{title}\n{content}\n")