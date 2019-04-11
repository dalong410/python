# ���� 8:08 2019-04-10 15����
# ���ϸ� : bs11.py



from bs4 import BeautifulSoup 

# HTML ���α׷� �ۼ� (���� ���, Ȩ��������� �����Ѵ�.)

html = """
<html><body>
  <ul>
    <li><a href="https://www.naver.com">naver</a></li>
    <li><a href="https://www.daum.net">daum</a></li>
  </ul>
</body></html>
"""

# BeautifulSoup ���̺귯���� ���� �ִ� Ȩ������ HTML �ҽ��� �м��� �����Ѵ�.
# HTML �м��ϱ� ------------------------------------------------- (��1)
soup = BeautifulSoup(html, 'html.parser')


# find_all() �޼���� �����ϱ� ---------------------------------- (��2)
# 2���� <a> �±׸� ��� ã�Ƴ��� links��� ������ ��Ƴ��´�.

links = soup.find_all("a")



# ��ũ ��� ����ϱ� --------------------------------------------- (��3)
# ���� a�� ����ڰ� ���Ƿ� ������ �� �ִ�. (�������, C���� �ַ� i or x������ ���� ����Ѵ�)
# links���� a �±װ� 2���� �����Ƿ� 2�� �ݺ��Ѵ�.

for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)

----------------------------------------------------------------------------------------------------------

# ���ϸ� : bs12.txt
# DOM(Docurnent Object Model) : XML �Ǵ� HTML�� ��ҿ� �����ϴ� ������ �ǹ��Ѵ�.
# DOM ����� �Ӽ� : �±� �̸��ڿ� �ִ� �� �Ӽ��� �ǹ��Ѵ�.
# <a>�� �Ӽ� href




>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<p><a href='a.html'>test</a></p>, html.parser")


# �м��� ����� �ƴ��� Ȯ���ϱ� -- (��1)
>>> soup.prettify()
 '<p>\n <a href="a.html">\n test\n </a>\n</p>'

>>> # <a> �±׸� ���� a�� �Ҵ�
>>> a = soup.p.a


# attrs �Ӽ��� �ڷ��� Ȯ�� -- (��2)
>>> type(a.attrs)
<class 'diet'>


# href �Ӽ��� �ִ��� Ȯ��
>>> 'href' in a.attrs
True

>>> # href �Ӽ� �� Ȯ��

>>> a ['href']
'a.html' 

--------------------------------------------------------------------------------------------------

====================================================================================
[�ǽ�] ������ ������ : http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp
====================================================================================

��ǥ : urlopen() & BeautifulSoup & request �����ϱ�


ex) ��ũ������ ���� -> ���û �߱⿹�� �����ϱ�

from bs4 import BeautifulSoup 
import urllib.request as req


url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

#url���� �˻��� �����͸� ��������
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

province = soup.find("province").string
tmEf  = soup.select_one("location > data > tmEf").string
wf2 = soup.select_one("location > data > wf").string


print("#province  =" + province.string)
print("#tmEf      =" + tmEf.string)
print("#wf2       =" + wf2.string)

----------------------------------------------------------------------------------------




























