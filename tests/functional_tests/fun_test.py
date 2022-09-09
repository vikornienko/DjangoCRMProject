
# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class SmokeSeleniumTestCase(StaticLiveServerTestCase):


    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome(
            executable_path='/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject/other_files/forwebdriver/chromedriver',
            service_log_path='/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject/other_files/forwebdriver/chromedriver.log'
        )
        cls.browser.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        super().tearDownClass()

    def testhomepage(self):
        self.browser.get(self.live_server_url)
        WebDriverWait(self.browser, 10)
        self.assertEqual(self.browser.title, "The install worked successfully! Congratulations!")