# 뭔가 잘 안됨 수정 필요함
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import pandas as pd

chrome_path = 'chromedriver.exe'
base_url = "https://www.google.co.kr/imghp"

# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--headless') # 창 없는 모드
# # headless 모드의 호환성을 위해 아래 옵션 추가(가끔 막는 웹이 있음)
# #chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
# chrome_options.add_argument("lang=ko_KR") # 한국어
# chrome_options.add_argument('window-size=1920x1080')
# # chrome_options.add_argument('--no-sandbox')
# # chrome_options.add_argument('--disable-dev-shm-usage')
#
#
# driver = webdriver.Chrome(chrome_path,chrome_options=chrome_options)
# driver.get(base_url)
# driver.implicitly_wait(3) # element가 로드될 때까지 지정한 시간만큼 대기할 수 있도록 설정
# driver.get_screenshot_as_file('google_screen.png')
# driver.close()

def selenium_scroll_option():
    SCROLL_PAUSE_SEC = 3

    # 스크롤 높이 가져옴
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 1초 대기
        time.sleep(SCROLL_PAUSE_SEC)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# 판콜에이내복액, 판피린티정
a = input("검색할 키워드를 입력 : ")
image_name = input("저장할 이미지 이름 : ")
driver = webdriver.Chrome(chrome_path)
driver.get('http://www.google.co.kr/imghp?hl=ko')
browser = driver.find_element_by_name("q")
browser.send_keys(a)
browser.send_keys(Keys.RETURN)

try:
    selenium_scroll_option() # 스크롤하여 이미지를 많이 확보
    driver.find_elements_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input')[0].click() # 이미지 더보기 클릭
    # Message: element not interactable
    # driver.find_elements_by_xpath('//input[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input')[0].click() # 이미지 더보기 클릭
    selenium_scroll_option()
except:
    print("test")


images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")  # 클래스 네임에서 공백은 .을 찍어줌
images_url = []
for i in images:
    if i.get_attribute('src') != None:
        images_url.append(i.get_attribute('src'))
    else:
        images_url.append(i.get_attribute('data-src'))
driver.close()

print("전체 다운로드한 이미지 개수: {}\n동일한 이미지를 제거한 이미지 개수: {}".format(len(images_url), len(pd.DataFrame(images_url)[0].unique())))
images_url=pd.DataFrame(images_url)[0].unique()
# print(images_url, len(images_url))

createFolder(image_name)
path = 'C:/Users/AI-00/PycharmProjects/startUpProject_1/' + image_name + '/'
for t, url in enumerate(images_url, 0):
    urllib.request.urlretrieve(url, path + (image_name + '_' + str(t) + '.jpg'))
    print(f"총 {len(images_url)}개 {t}개 만큼 진행 {(t/len(images_url)) * 100}")