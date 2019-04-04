#날씨 크롤링
import urllib.request
import urllib.parse
API = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"

# 매개변수를 URL 인코딩합니다.
values = {'zone' : '1130553500'}
params = urllib.parse.urlencode(values)

# 요청 전용 URL을 생성합니다
url = API + "?" + params
print("url=",url)

# 다운로드합니다
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

#### 참고 http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp?sido=1100000000&gugun=1130500000&dong=1130553500&x=22&y=5
