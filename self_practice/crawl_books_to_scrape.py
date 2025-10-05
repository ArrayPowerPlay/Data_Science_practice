from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import chromedriver_autoinstaller

# automatically install driver which appropriates with 
# current version of chrome in our laptop
driver_path = chromedriver_autoinstaller.install()

# initialize chrome
option = Options()
# use hidden chrome
option.add_argument("--headless")
# use chrome driver with the installed option
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=option)

url = "https://books.toscrape.com/"
driver.get(url)

# wait 2 secs for the web to load
time.sleep(2)

# use beautifulsoup to parse HTML source code
html = driver.page_source
# initialize beautifulsoup object to extract HTML information
soup = BeautifulSoup(html, "html.parser")
# extract list of books
books = soup.find_all("article", class_="product_pod")

# create a list to store data of each book
data = []

for book in books:
    # book name
    title = book.h3.a["title"]
    # book price
    price = book.find("p", class_="price_color").get_text()
    # book condition
    availability = book.find("p", class_="instock availability").get_text(strip=True)
    # save into a dictionary 
    data.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

# save data into file excel
df = pd.DataFrame(data)
df.to_excel("self_practice/books_data.xlsx", index=False)

# end chrome and quit session with webdriver
driver.quit()