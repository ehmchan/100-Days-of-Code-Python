from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time

phone = os.environ["phone"]
pw = os.environ["pw"]

chrome_driver_path = "C:\\Users\chane\OneDrive\Documents\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

link = "https://tinder.com/"

driver.get(link)
time.sleep(1)

sign_in = driver.find_element_by_xpath("//span[text()='Log in']")
sign_in.click()
time.sleep(1)

login_fb = driver.find_element_by_xpath("//span[text()='Log in with Facebook']")
login_fb.click()
time.sleep(1)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(5)
# print(driver.title)

login_email = driver.find_element_by_xpath('//*[@id="email"]')
login_email.send_keys(phone)
login_pw = driver.find_element_by_xpath('//*[@id="pass"]')
login_pw.send_keys(pw)
login_pw.send_keys(Keys.ENTER)
time.sleep(3)

driver.switch_to.window(base_window)

location = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[1]')
location.click()
time.sleep(1)

notif = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div/div/div[3]/button[2]')
notif.click()
time.sleep(1)

cookies = driver.find_element_by_xpath('//*[@id="t--1032254752"]/div/div[2]/div/div/div[1]/button')
cookies.click()
time.sleep(1)

for n in range(15):
    time.sleep(1)
    try:
        match = driver.find_element_by_xpath('//*[@id="t-619317887"]/div/div/div[1]/div/div[4]/button')
        match.click()
    except NoSuchElementException:
        try:
            add_home = driver.find_element_by_xpath('//*[@id="t-1222506740"]/div/div/div[2]/button[2]')
            add_home.click()
        except NoSuchElementException:
            try:
                super_like = driver.find_element_by_xpath('// *[ @ id = "t-1222506740"] / div / div / button[2]')
                super_like.click()
            except NoSuchElementException:
                like = driver.find_element_by_xpath(
                    '//*[@id="t--1032254752"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
                like.click()

driver.quit()
