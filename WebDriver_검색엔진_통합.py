# pip install selenium==3.0 설치 필요
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

# 원하는 검색어 입력
txt = input("원하는 검색어를 입력하세요 : ")
key = input("특정 검색 키워드를 입력하세요 : ")

# 원하는 검색엔진 선택
print("[1] Google")
print("[2] Bing")
print("[3] Zum")
print("[4] Naver")
print("[5] Nate")
print("[6] Daum")
src = int(input("원하는 검색엔진 번호를 입력하세요 : "))

# Chrome WebDriver를 이용해 Chrome을 실행합니다.
driver = webdriver.Chrome("E:/Python/Data/chromedriver")

## 조건문
# 선택한 검색엔진 홈페이지로 이동합니다.
# html element 이름이 q(query)인 것을 찾습니다.
if src == 1 : 
    driver.get("https://www.google.com")
    inputElement = driver.find_element_by_name("q")

elif src == 2 : 
    driver.get("https://www.bing.com")
    inputElement = driver.find_element_by_name("q")

elif src == 3 :
    driver.get("http://www.zum.com")
    inputElement = driver.find_element_by_name("query")

elif src == 4 : 
    driver.get("https://www.naver.com")
    inputElement = driver.find_element_by_name("query")

elif src == 5 :
    driver.get("https://www.nate.com")
    inputElement = driver.find_element_by_name("q")

elif src == 6 :
    driver.get("https://www.daum.net")
    inputElement = driver.find_element_by_name("q")

# 검색창에 입력했던 검색어를 입력합니다.
inputElement.send_keys(txt)
time.sleep(2)
# 검색내용을 보냅니다.
inputElement.submit()
time.sleep(2)
# 검색된 리스트 중 링크 텍스트에 키워드가 포함된 것을 찾습니다.
continue_link = driver.find_element_by_partial_link_text(key)
time.sleep(2)
# 해당 링크를 클릭합니다.
continue_link.click()
time.sleep(5)
# WebDriver를 종료합니다. (브라우저 닫기)
driver.quit()