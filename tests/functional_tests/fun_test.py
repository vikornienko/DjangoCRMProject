import time

from selenium import webdriver

browser = webdriver.Chrome(executable_path="/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject/other_files/forwebdriver/chromedriver")
try:
    browser.get('http://127.0.0.1:8000/')
    time.sleep(10)

except Exception as ex_error:
    print(ex_error)
finally:
    browser.close()
    browser.quit()