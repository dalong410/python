# 오후 8:08 2019-04-10 15일차
# 파일명 : bs11.py



from bs4 import BeautifulSoup 

# HTML 프로그램 작성 (예를 들어, 홈페이지라고 가정한다.)

html = """
<html><body>
  <ul>
    <li><a href="https://www.naver.com">naver</a></li>
    <li><a href="https://www.daum.net">daum</a></li>
  </ul>
</body></html>
"""

# BeautifulSoup 라이브러리가 위에 있는 홈페이지 HTML 소스의 분석을 시작한다.
# HTML 분석하기 ------------------------------------------------- (※1)
soup = BeautifulSoup(html, 'html.parser')


# find_all() 메서드로 추출하기 ---------------------------------- (※2)
# 2개의 <a> 태그를 모두 찾아내어 links라는 변수에 담아놓는다.

links = soup.find_all("a")



# 링크 목록 출력하기 --------------------------------------------- (※3)
# 변수 a는 사용자가 임의로 지정할 수 있다. (예를들어, C언어는 주로 i or x변수를 자주 사용한다)
# links에는 a 태그가 2개가 있으므로 2번 반복한다.

for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)

----------------------------------------------------------------------------------------------------------

# 파일명 : bs12.txt
# DOM(Docurnent Object Model) : XML 또는 HTML의 요소에 접근하는 구조를 의미한다.
# DOM 요소의 속성 : 태그 이름뒤에 있는 각 속성을 의미한다.
# <a>의 속성 href




>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<p><a href='a.html'>test</a></p>, html.parser")


# 분석이 제대로 됐는지 확인하기 -- (※1)
>>> soup.prettify()
 '<p>\n <a href="a.html">\n test\n </a>\n</p>'

>>> # <a> 태그를 변수 a에 할당
>>> a = soup.p.a


# attrs 속성의 자료형 확인 -- (※2)
>>> type(a.attrs)
<class 'diet'>


# href 속성이 있는지 확인
>>> 'href' in a.attrs
True

>>> # href 속성 값 확인

>>> a ['href']
'a.html' 

--------------------------------------------------------------------------------------------------

====================================================================================
[실습] 가져올 데이터 : http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp
====================================================================================

목표 : urlopen() & BeautifulSoup & request 조합하기


ex) 스크레이핑 예제 -> 기상청 중기예보 추출하기

from bs4 import BeautifulSoup 
import urllib.request as req


url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

#url에서 검색한 데이터를 가져오기
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

province = soup.find("province").string
tmEf  = soup.select_one("location > data > tmEf").string
wf2 = soup.select_one("location > data > wf").string


print("#province  =" + province.string)
print("#tmEf      =" + tmEf.string)
print("#wf2       =" + wf2.string)

----------------------------------------------------------------------------------------





























