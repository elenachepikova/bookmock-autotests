import allure
from selenium.webdriver.common.by import By

from core import Assertions


class Footer(Assertions):
    FOOTER = (By.CSS_SELECTOR, "footer.bb-section")
    LOGO = (By.CSS_SELECTOR, ".mx-n2.d-flex.flex-wrap")
    FACEBOOK_ICON = (By.XPATH, '//*[@href="https://facebook.com/"]')
    INSTAGRAM_ICON = (By.XPATH, '//*[@href="https://www.instagram.com/"]')
    LINKEDIN_ICON = (By.XPATH, '//*[@href="https://linkedin.com/"]')
    ADDRESS = (By.CSS_SELECTOR, ".d-flex.py-1:first-of-type")
    EMAIL = (By.CSS_SELECTOR, ".d-flex.py-1:last-of-type")
    MESSAGE = (By.CSS_SELECTOR, ".px-2.mb-3")
    address_text = "ul. Starowiślna 17/2, 31-038 Kraków"
    email_text = "ec.estest01@gmail.com"
    message_text = "This site is created for testing purposes and can be used only by the site owner"

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Assert footer section elements presence")
    def assert_footer_is_displayed(self):
        self.assert_element_is_visible(self.FOOTER)
        self.assert_element_is_visible(self.LOGO)
        self.assert_element_is_visible(self.FACEBOOK_ICON)
        self.assert_element_is_visible(self.INSTAGRAM_ICON)
        self.assert_element_is_visible(self.LINKEDIN_ICON)
        self.assert_element_is_visible(self.ADDRESS)
        self.assert_element_is_visible(self.EMAIL)
        self.assert_element_is_visible(self.MESSAGE)
        self.assert_text(self.ADDRESS, self.address_text)
        self.assert_text(self.EMAIL, self.email_text)
        self.assert_text(self.MESSAGE, self.message_text)
