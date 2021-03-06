from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        speed_link = "https://www.speedtest.net/"
        self.driver.get(speed_link)
        time.sleep(1)

        self.go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go.click()
        time.sleep(60)

        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self, email, pw, prom_down, prom_up):
        twitter_link = "https://twitter.com/"
        self.driver.get(twitter_link)
        time.sleep(1)

        log_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div')
        log_in.click()
        time.sleep(2)

        email_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email_box.send_keys(email)

        pw_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pw_box.send_keys(pw)
        pw_box.send_keys(Keys.ENTER)
        time.sleep(2)

        tweet_text = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span')
        tweet_text.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {prom_down}down/{prom_up}up?")

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()
        time.sleep(1)

        self.driver.quit()
