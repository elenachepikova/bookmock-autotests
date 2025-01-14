import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Actions, Assertions
from data import DOMAIN, TITLE


class FAQPage(Actions):
    FAQ_BANNER = (By.ID, 'bb-section-5129296E-C40A-D154-19A2-1C532EAE724A')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}/faq'
        self.title = f'FAQ | {TITLE}'
        self.assertions = Assertions(self.driver)

    @allure.step('Open FAQ page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "FAQ" page is opened')
    def assert_page_is_displayed(self):
        self.assertions.assert_page_title_and_url(self.title, self.page)
        self.assertions.assert_element_is_visible(self.FAQ_BANNER)