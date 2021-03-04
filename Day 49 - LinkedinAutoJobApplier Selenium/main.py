from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time

email = os.environ["lin_email"]
pw = os.environ["lin_pw"]
phone = os.environ["phone"]

chrome_driver_path = "C:\\Users\chane\OneDrive\Documents\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

link = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=python%20developer"
driver.get(link)
time.sleep(2)

sign_in = driver.find_element_by_class_name("cta-modal__primary-btn")
sign_in.click()
time.sleep(2)

email_entry = driver.find_element_by_id("username")
email_entry.send_keys(email)
pw_entry = driver.find_element_by_id("password")
pw_entry.send_keys(pw)
enter_button = driver.find_element_by_class_name("from__button--floating")
enter_button.click()
time.sleep(3)

jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")

# saving jobs automatically
for job in jobs:
    job.click()
    time.sleep(2)

    try:
        save = driver.find_element_by_class_name("jobs-save-button")
        save.click()
        time.sleep(2)

    except NoSuchElementException:
        print("already applied")
        continue

time.sleep(2)
driver.quit()

# # applying to jobs automatically
# for job in jobs:
#     job.click()
#     time.sleep(1)
#
#     try:
#         apply = driver.find_element_by_xpath("//span[contains(@class, 'artdeco-button__text') and text()='Apply now']")
#         apply.click()
#         time.sleep(2)
#
#         phone_num = driver.find_element_by_class_name("ember-text-field")
#         phone_num.send_keys(phone)
#
#         next = driver.find_element_by_css_selector(".display-flex button")
#         next.click()
#         time.sleep(1)
#
#         progress = driver.find_element_by_class_name("t-black--light")
#
#         if progress.text == "50%":
#             review = driver.find_element_by_xpath("//span[contains(@class, 'artdeco-button__text') and text()='Review']")
#             review.click()
#             time.sleep(1)
#
#             submit = driver.find_element_by_xpath("//span[contains(@class, 'artdeco-button__text') and text()='Submit application']")
#             submit.click()
#
#             print("job applied")
#             time.sleep(1)
#         else:
#             cancel = driver.find_element_by_class_name("artdeco-modal__dismiss")
#             cancel.click()
#             time.sleep(1)
#
#             discard = driver.find_element_by_xpath("//span[contains(@class, 'artdeco-button__text') and text()='Discard']")
#             discard.click()
#
#             print("job skipped")
#             time.sleep(1)
#
#     except NoSuchElementException:
#         print("already applied")
#         continue
#
# time.sleep(2)
# driver.quit()
