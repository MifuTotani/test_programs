from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import chromedriver_binary
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
SLEEP = 3


#引数確認
import sys
args = sys.argv
if len(args) != 2: 
    print("usage: python ", args[0], " searchWord")
    exit(1)
search_string = args[1]


# ドライバ
# options = Options()
# options.add_argument('--headless')
# options.add_argument('window-size=1050,652')
driver = webdriver.Chrome()
# driver.set_window_size('1200', '1000')
driver.get("https://www.monotaro.com/")
# driver.get("https://www.benricho.org/Tips/browse_size.html")
# driver.implicitly_wait(SLEEP)
time.sleep(SLEEP) # 読み込み時間を考慮

# # ブラウザの操作
element_form = driver.find_element(By.NAME, 'q')
element_form.send_keys(search_string)
driver.find_element(By.NAME,'q').submit()
time.sleep(SLEEP)


results = []
flag = False
CLASS="SearchResultImageContainerColmn"
products = driver.find_elements(By.CLASS_NAME, CLASS)
cnt = 0
MAX_CNT = 10
for product in products:
    elements = product.text.splitlines()
    textLink = product.find_element(By.CLASS_NAME, 'TextLink')

    result = {}
    result['link'] = textLink.get_attribute('href')
    # result['brand'] = product.find_element(By.CLASS_NAME, 'BrandText').text
    result['productName'] = textLink.text
    result["yen"] = product.find_elements(By.CLASS_NAME, 'Price')[0].text
    result["yen2"] = product.find_elements(By.CLASS_NAME, 'Price')[1].text
    result["sendFee"] = "send_fee"
    
    print(result)
    cnt = cnt + 1
    if cnt >= MAX_CNT: break



driver.close()
driver.quit()