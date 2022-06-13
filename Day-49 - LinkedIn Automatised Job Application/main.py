# ................... Automating LinkedIn Job Application ...................... #
# Created and modified by N.S.Bhanuprakash on 05-05-2022 ....................... #
# This code helps us to save the jobs and follow the companies and doesn't include code for scrolling down #

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

# Initialising selenium webdriver to get to the required website
chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=s)
website = "https://www.linkedin.com/jobs/search/?" \
          "currentJobId=3061217047&f_LF=f_AL&geoId=102257491&keywords=python%20developer&" \
          "location=London%2C%20England%2C%20United%20Kingdom"
driver.get(url=website)

sign_in = driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary")
sign_in.click()

time.sleep(2)
username = driver.find_element(by=By.ID, value="username")
username.send_keys("nsbprakash95@gmail.com")
password = driver.find_element(by=By.ID, value="password")
password_value = os.getenv("password_value")
password.send_keys(password_value)

sign_in = driver.find_element(by=By.CLASS_NAME, value="btn__primary--large")
sign_in.click()

driver.maximize_window()
time.sleep(5)  # In this time of 5 seconds, scroll the total website inorder to load the full data


# Scrolling down .............................................................................................
# search_result = driver.find_element(By.CLASS_NAME, value="global-footer-compact__linkedin-logo")
# scroll_cor = 100
# for n in range(30):
#     driver.execute_script(f"arguments[0].scrollTo(0, {scroll_cor})", search_result)
#     scroll_cor += 100
#     time.sleep(0.5)
# ............................................................................................................

job_details = driver.find_elements(by=By.CLASS_NAME, value="job-card-list__title")
print(len(job_details))

# ................. Code to check for one single job .......................................... #
# job_details.click()
# time.sleep(1)
# save_job = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button span")
# save_job.click()
# time.sleep(5)
# follow_job = driver.find_element(by=By.CSS_SELECTOR, value=".ml5 span")
# follow_job.click()
# print("follow clicked")
# ............................................................................................ #


job_names = []
for job in job_details:
    job.click()
    time.sleep(0.5)
    save_job = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button span")
    save_job.click()
    time.sleep(3)  # In this time of three seconds, scroll down to load the "follow" button
    follow_job = driver.find_element(by=By.CSS_SELECTOR, value=".ml5 span")
    follow_job.click()
    job_names.append(job.text)

print(job_names)
