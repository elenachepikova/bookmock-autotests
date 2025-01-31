import allure
from selenium.webdriver.common.by import By

from core import Assertions
from data import DOMAIN, TITLE


class ContactPage(Assertions):
    CONTACT_US_BANNER = (By.ID, "bb-section-51292A57-9603-A922-BC8E-363F9F372AE4")
    CONTACT_US_SECTION = (By.ID, "bb-section-51292A58-BF7C-41C2-A137-AA892D924926")
    FIND_US_SECTION = (By.ID, "bb-section-51292A59-E3FC-802D-398A-7CA900B7C05F")
    FIRST_NAME_FIELD = (By.XPATH, '//*[@name="First Name"]')
    LAST_NAME_FIELD = (By.XPATH, '//*[@name="Last Name"]')
    EMAIL_FIELD = (By.XPATH, '//*[@name="Email"]')
    MESSAGE_FIELD = (By.XPATH, '//*[@name="Message"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')

    def __init__(self, driver):
        super().__init__(driver)
        self.page = f"{DOMAIN}/contact"
        self.title = f"CONTACT | {TITLE}"

    @allure.step("Open CONTACT page")
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "CONTACT" page is opened')
    def assert_page_is_displayed(self):
        self.assert_page_title_and_url(self.title, self.page)
        self.assert_element_is_visible(self.CONTACT_US_BANNER)
        self.assert_banner_title("CONTACT US")

    @allure.step('Assert "CONTACT" page elements are present')
    def assert_contact_page_ui(self):
        self.assert_page_is_displayed()
        self.assert_element_is_visible(self.CONTACT_US_SECTION)
        self.assert_element_is_visible(self.FIND_US_SECTION)
        self.assert_element_is_visible(self.FIRST_NAME_FIELD)
        self.assert_element_is_visible(self.LAST_NAME_FIELD)
        self.assert_element_is_visible(self.EMAIL_FIELD)
        self.assert_element_is_visible(self.SUBMIT_BUTTON)
        self.assert_element_is_visible(self.MESSAGE_FIELD)
