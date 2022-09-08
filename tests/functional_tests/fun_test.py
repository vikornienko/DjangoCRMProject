import time

from django.test import LiveServerTestCase
from selenium import webdriver


class SmokeSeleniumTestCase(LiveServerTestCase):

    def testhomepage(self):
        browser = webdriver.Chrome(executable_path="/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject/other_files/forwebdriver/chromedriver")
        try:
            browser.get('http://127.0.0.1:8000/')
            # browser.get('https://google.com')
            assert "The install worked successfully! Congratulations!" in browser.title
            time.sleep(10)


        except Exception as ex_error:
            print(ex_error)
        finally:
            browser.close()
            browser.quit()