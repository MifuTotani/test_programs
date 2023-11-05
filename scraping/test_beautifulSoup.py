import requests
from bs4 import BeautifulSoup

searchWord = "消しゴム"

url = "https://www.monotaro.com/" + searchWord
res = requests.get(url)


print(res.text)