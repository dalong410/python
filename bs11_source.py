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
