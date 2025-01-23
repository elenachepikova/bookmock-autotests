import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Assertions
from data import TITLE


class FormSubmittedPage(Assertions):
    FORM_SUBMITTED_SECTION = (By.ID, 'bb-section-form-confirmation-section-boilerplate')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.title = f'Form Submitted! | {TITLE}'

    @allure.step('Assert "Form Submitted!" page is opened')
    def assert_page_is_displayed(self):
        self.assert_page_title_and_url(self.title)
        self.assert_element_is_visible(self.FORM_SUBMITTED_SECTION)
