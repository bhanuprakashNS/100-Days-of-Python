# ................... Instagram Follower Bot ............................. #
# ............. Created and modified by N.S.Bhanuprakash on 09-05-2022 .....#

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
INSTAGRAM_EMAIL = "smtptrial22@gmail.com"
INSTAGRAM_PASSWORD = os.getenv("insta_password")
INSTAGRAM_WEBSITE = "https://www.instagram.com"
SEARCH_NAME = "divya_madhuri_y"
# "sumanth_gundeti"
TOTAL_FOLLOWS = 40
NUM_OF_FOLLOWS_ONCE = 8
S = Service(executable_path=CHROME_DRIVER_PATH)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=S)
        self.driver.get(url=INSTAGRAM_WEBSITE)
        sleep(1)
        self.driver.maximize_window()

    def login(self):
        """Logins into Instagram using the credentials"""
        sleep(2)
        username = self.driver.find_element(by=By.NAME, value="username")
        username.send_keys(INSTAGRAM_EMAIL)
        sleep(0.5)
        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys(INSTAGRAM_PASSWORD)
        sleep(0.5)
        password.send_keys(Keys.ENTER)
        sleep(4)
        skip_save = self.driver.find_element(by=By.CLASS_NAME, value="cmbtv")
        skip_save.click()
        sleep(4)
        not_now = self.driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/div[3]/button[2]")
        not_now.click()
        sleep(2)

    def find_followers(self, name):
        """Goes to the required person's profile and opens their follower's list"""
        sleep(2)
        url = f"https://www.instagram.com/{name}/"
        self.driver.get(url=url)
        sleep(2)
        followers = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/header/'
                                                                'section/ul/li[2]/a/div')
        followers.click()

    def follow(self):
        """Follows their followers one by one. After following all in one single pop up, scrolls up the pop up
        by one scroll height and begins again following the persons."""
        sleep(3)
        modal = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')
        for i in range(int(TOTAL_FOLLOWS/NUM_OF_FOLLOWS_ONCE)):
            sleep(5)
            for char in range(1, NUM_OF_FOLLOWS_ONCE):
                num = i * (NUM_OF_FOLLOWS_ONCE - 1) + char
                try:
                    try:
                        follower = self.driver.find_element(by=By.XPATH, value=f"/html/body/div[6]/div/div/div/div[2]/ul/div/"
                                                                               f"li[{num}]/div/div[3]/button/div")
                    except NoSuchElementException:
                        follower = self.driver.find_element(by=By.XPATH,
                                                            value=f"/html/body/div[6]/div/div/div/div[2]/ul/div/"
                                                                  f"li[{num}]/div/div[2]/button/div")
                        follower.click()
                    else:
                        follower.click()
                        sleep(2)
                except ElementClickInterceptedException:
                    cancel = self.driver.find_element(by=By.XPATH, value='/html/body/div[11]/div/div/div/'
                                                                         'div[3]/button[2]')
                    cancel.click()
                    sleep(2)

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)


instagram = InstaFollower()
instagram.login()
instagram.find_followers(name=SEARCH_NAME)
instagram.follow()
