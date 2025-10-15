from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service 
from bs4 import BeautifulSoup
import pandas as pd 
import time
import chromedriver_autoinstaller
import random

# lấy đường dẫn driver phù hợp với phiên bản chrome hiện tại
driver_path = chromedriver_autoinstaller.install()

option = Options()
option.add_argument("--headless")
service = Service(driver_path)

# sử dụng driver với các tham số khởi tạo
driver = webdriver.Chrome(service=service, options=option)

# url cần crawl
url = 'https://cafef.vn/tai-chinh-quoc-te.chn'