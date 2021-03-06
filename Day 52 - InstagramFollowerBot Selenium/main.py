import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from random import randint

SIMILAR_ACCOUNT = "csaffitz"
USERNAME = os.environ["username"]
PW = os.environ["pw"]
chrome_driver_path = "C:\\Users\chane\OneDrive\Documents\Development\chromedriver.exe"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)

        user_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_input.send_keys(USERNAME)

        pw_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pw_input.send_keys(PW)
        pw_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(1)

        list_followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
        list_followers.click()
        time.sleep(2)

        element_inside_popup = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element_inside_popup)
            time.sleep(1)

    def follow(self):
        followers = self.driver.find_elements_by_class_name("Pkbci")
        for follower in followers:
            try:
                follower.click()
                time.sleep(randint(1, 6))
            except ElementClickInterceptedException:
                unfollow = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                unfollow.click()
                time.sleep(1)
        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
