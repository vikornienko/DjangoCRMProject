
from django.test import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


class SmokeSeleniumTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='/home/vikornienko/PycharmProjects/learningDjango/DjangoCRMProject/other_files/forwebdriver/chromedriver')
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        super().tearDownClass()

    def testhomepage(self):
        self.selenium.get('http://127.0.0.1:8000/')
        assert "The install worked successfully! Congratulations!" in self.selenium.title
