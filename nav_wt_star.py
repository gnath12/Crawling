import requests
from bs4 import BeautifulSoup as bs

url = "https://comic.naver.com/webtoon/weekday"

r = requests.get(url)

soup = bs(r.text, "html.parser")

weeklist_link = soup.select("ul[class=category_tab] > li")
new_url = []
nav_web = dict()
# 요일별 웹툰
for link in weeklist_link:
    weekname = link.select("a")[0].attrs["href"]

    new_url.append("https://comic.naver.com"+weekname)

# 정렬 기준
for week_list in new_url[1:-1]:
    r = requests.get(week_list)
    soup = bs(r.text, "html.parser")

    web_list = soup.select("ul[class=img_list] > li")
    for web in web_list:
        title = soup.select("div[class=thumb] > a")[0].attrs["title"]
    #     st_scr = soup.select("div[class=rating_type] > strong")[0].text
    
        print(title)



        # with open("uak.txt", "w", encoding="UTF-8") as f:
        #     for title, st_scr in nav_web.items():
        #         f.write(f"{title}{st_scr}\n")