# 네이버 로그인
# pip install selenium==3.0

from selenium import webdriver

url = "https://nid.naver.com/nidlogin.login"

# PhantomJS 드라이버 추출하기 --- (※1)
browser = webdriver.PhantomJS()

# 3초 대기하기 --- (※2)
browser.implicitly_wait(3)

# URL 읽어 들이기 --- (※3)
browser.get(url)
element_id = browser.find_element_by_id("id")
element_id.clear()
element_id.send_keys("id 입력하세요")
element_pw = browser.find_element_by_id("pw")
element_pw.clear()
element_pw.send_keys("pw 입력하세요")

# 화면을 캡처해서 저장하기 --- (※4)
browser.save_screenshot("naver5.png")
print("저장")

# 브라우저 종료하기 --- (※5)
browser.quit()
