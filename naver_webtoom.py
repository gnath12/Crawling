import requests
from bs4 import BeautifulSoup as bs

url = "https://comic.naver.com/webtoon/weekday"

r = requests.get(url)

soup = bs(r.text, "html.parser")

weeklist_name = soup.select("div[class=col_inner]")



#요일 이름 가져오기
for weeklist in weeklist_name:
    day = weeklist.select("h4")[0].text
    file_name = day + ".txt"
    link = weeklist.select("ul > li > div[class=thumb]")
    nav_web = dict()
    #요일별 웹툰 링크
    for list_link in link:
        list = list_link.select("a")[0].attrs["href"]
        nodab = "https://comic.naver.com" + list

        r = requests.get(nodab)
        soup = bs(r.text, "html.parser")

        title = soup.select("span[class=title]")[0].text
        writer = soup.select("span[class=wrt_nm]")[0].text

        nav_web.update({title:writer})




    print(f"{day} {len(title)}개 중 {}개 크롤링 중... {}%", end="\r")



    with open(file_name, "w", encoding="UTF-8") as f:
        for title, writer in nav_web.items():
            f.write(f"{title}\n{writer}\n")

