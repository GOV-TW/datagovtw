# get.py 2020.05.05
# 取得 data.gov.tw 網站的基礎分類清單
# 建立 Data\dtid_list.csv
#

import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.today()
today = now.date()

print(today)
