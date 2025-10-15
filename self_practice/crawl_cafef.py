from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import chromedriver_autoinstaller

driver_path = chromedriver_autoinstaller.install()

option = Options()
# option.add_argument("--headless")
service = Service(driver_path)

driver = webdriver.Chrome(options=option, service=service)

url = "https://cafef.vn/xa-hoi.chn"
driver.get(url)

time.sleep(3)

html = driver.page_source
# initialize beautifulsoup object to extract HTML information
soup = BeautifulSoup(html, "html.parser")
news = soup.find_all("div", class_="tlitem box-category-item")

data = [] 

for new in news:
    # news title
    title = new.h3.a.get_text(strip=True)
    time_post = new.find("div", class_="knswli-right").span["title"]
    summary = new.find("div", class_="knswli-right").p.get_text(strip=True)
    base_link = "https://cafef.vn"
    link = base_link + new.find("a", class_=["avatar", "img-resize"])["href"]

    data.append({
        "Title": title, 
        "Time": time_post,
        "Summary": summary,
        "Link": link
    })

df = pd.DataFrame(data)
df.to_excel("self_practice/news_cafef.xlsx", index=False)

driver.quit()