"""from bs4 import BeautifulSoup

html='''
<html>
<body>
    <h1 id='title'>스크레이핑</h1>
    <p id='body'>웹 페이지를 분석</p>
    <p>원하는 부분을 추출</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

'''h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)

h1 = soup.find(id='title')
p1 = soup.find(id='body')
print("title = " + h1.string)
print("body = " + p1.string)'''

import urllib.request as req
from bs4 import BeautifulSoup

url = "https://www.netflix.com/kr/browse/genre/839338"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

news = soup.find(id='today_main_news')
head_lines = soup.select("span.nm-collections-title-name")
for head_line in head_lines:
    print(head_line.string)
#print(news)"""

import urllib.request as req
from bs4 import BeautifulSoup


url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

rank_keywords = soup.select('div.jcarousel._realtime_new_list_carousel.carousel_line_r > div > div > div > ul > li > a > span[class*=title]')
print(rank_keywords)
for rank_keyword in rank_keywords :
    print(rank_keyword.string)