import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Actions, Assertions
from data import DOMAIN, TITLE


class AboutPage(Actions):
    ABOUT_US_BANNER = (By.ID, 'bb-section-5129237E-F62C-D51F-8FF0-2BFF121EE5F7')
    CONTACT_US = (By.XPATH, '//button[contains(text(),"CONTACT US")]')
    SHOP_NOW = (By.CSS_SELECTOR, 'button.btn-secondary')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}about'
        self.title = f'ABOUT | {TITLE}'
        self.assertions = Assertions(self.driver)

    @allure.step('Open About page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "About" page is opened')
    def assert_page_is_displayed(self):
        self.assertions.assert_page_title_and_url(self.title, self.page)
        self.assertions.assert_element_is_visible(self.ABOUT_US_BANNER)
