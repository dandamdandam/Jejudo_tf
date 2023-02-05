import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

# usb 가져오지 못한다는 에러 자꾸 떠서 추가함
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

#폴더 생성(로컬디스크 C에)
if not os.path.isdir("datas") :
    print('폴더 생성 완료')
    os.mkdir("datas")
else:
    print("이미 동일한 이름의 폴더가 있습니다")

driver = webdriver.Chrome("C:/Users/dy/Desktop/eyecontect/chromedriver.exe")
driver.get("https://yandex.com/images/search?text=udo%20island&lr=114230") #검색한 사이트 자체 넣기
# elem = driver.find_element(By.NAME, "q") #검색창 찾음
# elem.send_keys("kayak") #키보드 입력값
# elem.send_keys(Keys.RETURN) #엔터키

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

f=open('text.txt', 'w') #이미지 설명하는 글 텍스트로 파일에 써줌.

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#-------------------------------------------------------사진사이트
images = driver.find_elements_by_css_selector(".serp-item__link>img")#클래스 가진거 모두 선택
count = 440
for image in images:
    time.sleep(2)
    try:
        urllib.request.urlretrieve(image.get_attribute("src"), "C:/JDY/EC_data/이미지/"+"섬" + str(count) + ".jpg")
        f.write(str(count)+". "+image.get_attribute("alt")+"\n")
        count = count + 1
    except:
        pass
'''
#------------------------------------------------------구글
images = driver.find_elements_by_css_selector(".bRMDJf.islir>img")#클래스 가진거 모두 선택
count = 203
for image in images:
    time.sleep(2)
    try:
        urllib.request.urlretrieve(image.get_attribute("src"), "C:/JDY/EC_data/이미지/섬" + str(count) + ".jpg")
        f.write(str(count)+". "+image.get_attribute("alt")+"\n")
        count = count + 1
    except:
        pass

#------------------------------------------------------네이버
images = driver.find_elements_by_css_selector(".thumb>img")#클래스 가진거 모두 선택
count = 410
for image in images:
    time.sleep(2)
    try:
        urllib.request.urlretrieve(image.get_attribute("src"), "C:/JDY/EC_data/이미지/섬" + str(count) + ".jpg")
        f.write(str(count)+". "+image.get_attribute("alt")+"\n")
        count = count + 1
    except:
        pass
'''
f.close()
driver.close()