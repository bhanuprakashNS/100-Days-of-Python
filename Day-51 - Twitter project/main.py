# ................... Twitter Complaining Bot ............................. #
# ............. Created and modified by N.S.Bhanuprakash on 07-05-2022 .....#

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

PROMISED_DOWN = 40
PROMISED_UP = 41
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_EMAIL = "smtptrial22@gmail.com"
TWITTER_PASSWORD = "Smgmail@1995"
SPEEDTEST_WEBSITE = "https://www.speedtest.net/"
TWITTER_WEBSITE = "https://twitter.com/i/flow/login"
S = Service(executable_path=CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=S)
        self.up = ""
        self.down = ""

    def speed_test_start(self):
        """ Initialises speedtest website and starts the speed test"""
        self.driver.get(url=SPEEDTEST_WEBSITE)
        sleep(4)
        try:
            go_button = self.driver.find_element(by=By.CLASS_NAME, value="js-start-test")
        except NoSuchElementException:
            print("Go button not found")
        else:
            go_button.click()
        return self.get_speed_values()

    def get_speed_values(self):
        """Obtains the download and upload speed values"""
        check_speed = True
        # While loop to check every 5 seconds whether the speed test is completed or not and get the required values.
        while check_speed:
            sleep(5)
            download_speed = self.driver.find_element(by=By.CLASS_NAME, value="download-speed")
            self.down = download_speed.text
            upload_speed = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed")
            self.up = upload_speed.text
            if len(self.up) >= 5:   # Ex- if speed = 38.51 Mbps, len(speed) is 5
                check_speed = False
        speed_values = [float(self.down), float(self.up)]
        return speed_values

    def tweet_at_provider(self):
        """ Tweets the internet speed obtained to the ISP"""
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url=TWITTER_WEBSITE)
        sleep(5)
        email = self.driver.find_element(by=By.NAME, value='text')
        email.send_keys("smtptrial22@gmail.com")
        sleep(0.5)
        email.send_keys(Keys.ENTER)
        sleep(2)
        try:
            self.driver.find_element(by=By.NAME, value='password')
        except NoSuchElementException:
            sleep(0.5)
            username = self.driver.find_element(by=By.NAME, value='text')
            twitter_username = os.getenv("username")
            username.send_keys(twitter_username)
            username.send_keys(Keys.ENTER)
        finally:
            sleep(0.5)
            password = self.driver.find_element(by=By.NAME, value='password')
            twitter_password = os.getenv("password")
            password.send_keys(twitter_password)
            password.send_keys(Keys.ENTER)
        sleep(4)
        tweet_msg = self.driver.find_element(by=By.CLASS_NAME, value="public-DraftStyleDefault-ltr")
        tweet_msg.send_keys(f"Present download speed of my ISP is {self.down}Mbps and upload speed is {self.up}Mbps")
        tweet = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/'
                                                            'div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                            'div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()


tweet_bot = InternetSpeedTwitterBot()
speeds = tweet_bot.speed_test_start()
present_download_speed = speeds[0]
present_upload_speed = speeds[1]
print(speeds)

if present_download_speed < PROMISED_DOWN or present_upload_speed < PROMISED_UP:
    tweet_bot.tweet_at_provider()





