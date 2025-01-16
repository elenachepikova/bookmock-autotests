import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Actions, Assertions


class Footer(Actions):
    FOOTER = (By.CSS_SELECTOR, 'footer.bb-section')
    LOGO = (By.CSS_SELECTOR, '.mx-n2.d-flex.flex-wrap')
    FACEBOOK_ICON = (By.XPATH, '//*[@href="https://facebook.com/"]')
    INSTAGRAM_ICON = (By.XPATH, '//*[@href="https://www.instagram.com/"]')
    LINKEDIN_ICON = (By.XPATH, '//*[@href="https://linkedin.com/"]')
    ADDRESS = (By.CSS_SELECTOR, '.d-flex.py-1:first-of-type')
    EMAIL = (By.CSS_SELECTOR, '.d-flex.py-1:last-of-type')
    MESSAGE = (By.CSS_SELECTOR, '.px-2.mb-3')
    address_text = 'ul. Starowiślna 17/2, 31-038 Kraków'
    email_text = 'ec.estest01@gmail.com'
    message_text = 'This site is created for testing purposes and can be used only by the site owner'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.assertions = Assertions(self.driver)
        self.address = self.get_element(self.ADDRESS)
        self.email = self.get_element(self.EMAIL)
        self.message = self.get_element(self.MESSAGE)

    @allure.step('Assert that all footer section elements are present')
    def assert_footer_is_displayed(self):
        self.assertions.assert_element_is_visible(self.FOOTER)
        self.assertions.assert_element_is_visible(self.LOGO)
        self.assertions.assert_element_is_visible(self.FACEBOOK_ICON)
        self.assertions.assert_element_is_visible(self.INSTAGRAM_ICON)
        self.assertions.assert_element_is_visible(self.LINKEDIN_ICON)
        self.assertions.assert_element_is_visible(self.ADDRESS)
        self.assertions.assert_element_is_visible(self.EMAIL)
        self.assertions.assert_element_is_visible(self.MESSAGE)
        self.assertions.assert_text(self.address, self.address_text)
        self.assertions.assert_text(self.email, self.email_text)
        self.assertions.assert_text(self.message, self.message_text)
