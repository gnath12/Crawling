import requests
from bs4 import BeautifulSoup as bs

url = "https://news.daum.net"

r = requests.get(url)

babo = bs(r.text, "html.parser")

url_list = babo.select("ul[class=list_todayseries] > li")

sung = dict()

for i in url_list:
    sam = i.select("a[class=link_txt]")[0].attrs["href"]

    r = requests.get(sam)
    babo = bs(r.text, "html.parser")

    title = babo.select("h3[class=tit_view]")[0].text

    contains = ""
    for elem in babo.select("span[class=info_view] > span[class=txt_info]"):
        contains += elem.text+" "


    # idx = 0
    # for c in contains:
    #     if c.isdigit():
    #         break
    #     idx += 1

    # author = contains[:idx].replace("입력", "").replace("기자", "").strip()
    # date = contains[idx:].strip()
    # print(f"author : {author}\tdate:{date}")
    sung.update({title:contains})

# print(sung)
with open("wow.txt", "w", encoding="UTF-8") as f:
    for title, contains in sung.items():
        f.write(f"{title}\n{contains}\n")


