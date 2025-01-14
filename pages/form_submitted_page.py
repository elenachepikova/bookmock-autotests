import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core.actions import Actions
from core.assertions import Assertions
from data.test_data import TITLE


class FormSubmittedPage(Actions):
    FORM_SUBMITTED_SECTION = (By.ID, 'bb-section-form-confirmation-section-boilerplate')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.title = f'Form Submitted! | {TITLE}'
        self.assertions = Assertions(self.driver)

    @allure.step('Assert "Form Submitted!" page is opened')
    def assert_page_is_displayed(self):
        self.assertions.assert_page_title(self.title)
        self.assertions.assert_element_is_visible(self.FORM_SUBMITTED_SECTION)
