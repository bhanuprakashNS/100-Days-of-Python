# ............... Cookie Clicker Game ................................. #
# ..........Created and modified by N.S.Bhanuprakash on 03-05-2022 .............#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Initialising selenium webdriver to get to the required website
chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)
website = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=website)

present_time = time.time()
num_sec_from_now = 60*1          # Number of seconds of game to be run
timeout = time.time() + num_sec_from_now
cookie = driver.find_element(by=By.ID, value="cookie")

# .......... Meta data to test the code with-out scraping the website frequently ........... #
# chefs_prices = {'Cursor': 15, 'Grandma': 100, 'Factory': 500, 'Mine': 2000, 'Shipment': 7000,
#                 'Alchemy lab': 50000, 'Portal': 1000000, 'Time machine': 123456789}
# key = list(chefs_prices.keys())[list(chefs_prices.values()).index(123456789)]
# button = driver.find_element(by=By.ID, value=f"buy{key}")
# print(button.get_attribute("class"))
# print(max(list(chefs_prices.values())))
# max_price = 0
# for key, value in chefs_prices.items():
#     max_price = max(max_price, int(value.replace(",", "")))
#     print(key, value)
# print(max_price)
# ........................................................................................... #

while True:
    # time.sleep(0.5)
    cookie.click()
    score = driver.find_element(by=By.ID, value="money")
    score = int(score.text)

    # For every 5 seconds from present time, buy the available chefs
    if int(time.time() - present_time) % 5 == 0:
        # print("small break")
        cookie_chefs = driver.find_elements(by=By.CSS_SELECTOR, value="#rightPanel div b")
        chefs_prices = {}
        # Getting Un-grayed chef details and their cost and writing them to a dict
        for chef in cookie_chefs:
            if chef.text != "":
                chef_details = chef.text.split()
                key = chef_details[0]
                if len(chef_details) == 3:
                    pass
                else:
                    for num in range(1, len(chef_details) - 2):
                        key = key + " " + chef_details[num]
                available_cookie_chefs = driver.find_element(by=By.ID, value=f"buy{key}")
                available_cookie_chef_class = available_cookie_chefs.get_attribute("class")
                if available_cookie_chef_class != "grayed":
                    chefs_prices[key] = int(chef_details[-1].replace(",", ""))

        # Finding the max price among the available cookie chefs
        max_price = 0
        for key, value in chefs_prices.items():
            max_price = max(max_price, value)
            # print(key, value)
        # print(max_price)
        # Buying the maximum priced chef if we have the sufficient score(money)
        if score > max_price:
            if max_price in list(chefs_prices.values()):
                click_key = list(chefs_prices.keys())[list(chefs_prices.values()).index(max_price)]
                button = driver.find_element(by=By.ID, value=f"buy{click_key}")
                button.click()
                print(f"{(click_key, max_price)} is the maximum available in a list of {chefs_prices}")

        # Stopping the game after the required time and getting the cookie/sec value
        if int(time.time() - timeout) % num_sec_from_now == 0:
            print(f"Strategic Timeout!! - {round((time.time() - present_time)/60, 1)} min")
            total_score_now = driver.find_element(by=By.ID, value="cps")
            print(f'Total {total_score_now.text}')
            break
