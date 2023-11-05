import requests
from bs4 import BeautifulSoup



url = 'https://www.yomiuri.co.jp'
url = "https://www.monotaro.com/s/?c=&q=%E6%B6%88%E3%81%97%E3%82%B4%E3%83%A0"
res = requests.get(url)


print(res.text)