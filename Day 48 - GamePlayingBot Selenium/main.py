from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\\Users\chane\OneDrive\Documents\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

click_cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
end = time.time() + 60*5

while True:
    click_cookie.click()

    if time.time() > timeout:
        store = driver.find_elements_by_css_selector("#store div")
        for item in store[::-1]:
            if item.get_attribute("class") != "grayed":
                item.click()
                break
        timeout += 5

    if time.time() > end:
        cps = driver.find_element_by_id("cps").text
        print(cps)
        break

