
from django.test import LiveServerTestCase
from selenium import webdriver


class SmokeSeleniumTestCase(LiveServerTestCase):

    # dbsettings = development.DATABASES
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome(
            executable_path='/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject/other_files/forwebdriver/chromedriver',
            service_log_path='/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject/other_files/forwebdriver/chromedriver.log'
        )
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        super().tearDownClass()

    def testhomepage(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert "The install worked successfully! Congratulations!" in self.browser.title
