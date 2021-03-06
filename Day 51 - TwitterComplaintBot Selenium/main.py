import os

from TwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
EMAIL = os.environ["email"]
PW = os.environ["pw"]
chrome_driver_path = "C:\\Users\chane\OneDrive\Documents\Development\chromedriver.exe"

bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider(EMAIL, PW, PROMISED_DOWN, PROMISED_UP)
