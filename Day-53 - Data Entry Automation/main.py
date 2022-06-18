# ................... Data Entry Automation ................................ #
# ............. Created and modified by N.S.Bhanuprakash on 10-05-2022 .....#

from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

scrape_website = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22" \
                 "mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%" \
                 "22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22mapZoom%22%3A11%2C%22" \
                 "isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%" \
                 "22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%" \
                 "7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%" \
                 "22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%" \
                 "3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

google_form_url = "https://forms.gle/kCxhDDyEe5wtMa4h9"
chrome_driver_path = "C:\Development\chromedriver.exe"

# .................. Getting HTML file using Requests module ................................................ #
# Note that we will get only few data (9 entries) because only 9 of the total list is loaded. If you want many
# data sets, you have to use selenium to scroll the page and load more data.

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)"
#                   " Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
# response = requests.get(url=scrape_website, headers=header)
# data = response.text
# ........................................................................................................... #

# .............. Code to get HTML file using selenium to parse it using Beautiful Soup ................. #
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(url=scrape_website)
driver.maximize_window()
sleep(2)
modal = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/div/div/div[1]')
# for i in range(4):   # Scrolls down the website 8 number of times
#     sleep(3)
driver.execute_script("arguments[0].scrollTop = 4200", modal)
HTML = driver.page_source
with open("website.html", "w", encoding="utf-8") as file:
    file.write(HTML)
driver.close()
# ...................................................................................................... #
# .............. Gets all the values of prices, addresses and links using Beautiful Soup ................. #
with open("website.html", "r") as file:
    HTML = file.read()
soup = BeautifulSoup(HTML, "html.parser")

links = []
for link in soup.find_all(name="a", class_="list-card-img"):
    href = link.get("href").strip()
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)
print(len(links), links)

prices = []
for element in soup.find_all(class_="list-card-price"):
    prices.append(int(element.text.split("$")[1].replace(",", "")[0:4]))
print(len(prices), prices)

addresses = []
for address in soup.find_all(class_="list-card-addr"):
    address = address.text.split()
    address = " ".join(address)
    addresses.append(address)
print(len(addresses), addresses)
# ...................................................................................................... #
# ................. Opens Google form and enters all the data obtained ................................. #
s = Service(executable_path=chrome_driver_path)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=chr_options)
driver.get(url=google_form_url)
sleep(1)
driver.maximize_window()

for num in range(len(addresses)):
    sleep(1)
    find_address = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/"
                                                          "div[2]/div/div[1]/div/div[1]/input")
    find_address.send_keys(addresses[num])
    sleep(0.5)
    find_price = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/"
                                                        "div[2]/div/div[1]/div/div[1]/input")
    find_price.send_keys(prices[num])
    sleep(0.5)
    find_link = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/"
                                                       "div[2]/div/div[1]/div/div[1]/input")
    find_link.send_keys(links[num])
    sleep(0.5)
    find_submit = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/"
                                                         "div/span/span")
    find_submit.click()
    sleep(1)
    if num != len(addresses)-1:
        another_response = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        another_response.click()
    else:
        pass




