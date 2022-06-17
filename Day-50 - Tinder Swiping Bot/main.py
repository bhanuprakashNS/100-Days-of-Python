# ................... Auto Tinder Swiping Bot ...................... #
# Created and modified by N.S.Bhanuprakash on 06-05-2022 ....................... #

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# Initialising selenium webdriver to get to the required website
chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)
instant_website = "https://tinder.com/deeplink/account-recovery/confirm/eyJhbGciOiJIUzI1NiJ9.bnNicHJha2FzaDk1QGhvdG" \
                  "1haWwuY29tLXJlY292ZXJ5X2VtYWlsX290cA.5zKUmCYtudoBBRgp2PrkFQ2ekBeEqf2y0-iH4XSCeDY"
main_website = "https://tinder.com/"
website = main_website
driver.get(url=website)
driver.maximize_window()

# ................. Use this when website is main_website ......................................#
sleep(5)  # 10 sec because giving time to manually close instant link popup msg
login = driver.find_element(by=By.LINK_TEXT, value="Log in")
login.click()
sleep(3)
more_options = driver.find_element(by=By.XPATH, value="//*[@id='c-528371988']/"
                                                      "div/div/div[1]/div/div/div[3]/span/button")
more_options.click()
sleep(2)
login_phone = driver.find_element(by=By.XPATH, value="//*[@id='c-528371988']/"
                                                     "div/div/div[1]/div/div/div[3]/span/div[3]/button/span[2]")
login_phone.click()
# ............................................................................................. #

sleep(15)
phone_number = os.getenv("phonenumber")
input_number = driver.find_element(by=By.XPATH, value="//*[@id='c-528371988']/div/div/div[1]/div/div[2]/div/input")
input_number.send_keys("phonenumber")
input_number.send_keys(Keys.ENTER)
sleep(60)  # 60 sec, because we need to enter OTPs received on mobile and email manually
location = driver.find_element(by=By.XPATH, value="//*[@id='c-528371988']/div/div/div/div/div[3]/button[1]/span")
location.click()

privacy_consent = driver.find_element(by=By.XPATH, value="//*[@id='c1200009088']/"
                                                         "div/div[2]/div/div/div[1]/div[1]/button/span")
privacy_consent.click()
sleep(2)
notification_consent = driver.find_element(by=By.XPATH, value='//*[@id="c-528371988"]/'
                                                              'div/div/div/div/div[3]/button[2]/span')
notification_consent.click()
sleep(4)

for _ in range(5):
    try:
        webdriver.ActionChains(driver).send_keys(Keys.ARROW_LEFT).perform()
    except NoSuchElementException:
        print("You couldn't access the property exactly")
    except ElementClickInterceptedException:
        driver.find_element(By.CSS_SELECTOR, ".itsAMatch a").click()
    finally:
        sleep(2)
