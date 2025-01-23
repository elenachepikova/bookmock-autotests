import time

import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Assertions
from data import DOMAIN, TITLE


class ContactPage(Assertions):
    CONTACT_US_BANNER = (By.ID, 'bb-section-51292A57-9603-A922-BC8E-363F9F372AE4')
    CONTACT_US_SECTION = (By.ID, 'bb-section-51292A58-BF7C-41C2-A137-AA892D924926')
    FIND_US_SECTION = (By.ID, 'bb-section-51292A59-E3FC-802D-398A-7CA900B7C05F')
    FIRST_NAME_FIELD = (By.XPATH, '//*[@name="First Name"]')
    LAST_NAME_FIELD = (By.XPATH, '//*[@name="Last Name"]')
    EMAIL_FIELD = (By.XPATH, '//*[@name="Email"]')
    MESSAGE_FIELD = (By.XPATH, '//*[@name="Message"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')

    def __init__(self, driver, customer_data=None):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}/contact'
        self.title = f'CONTACT | {TITLE}'
        self.customer_data = customer_data

    @allure.step('Open CONTACT page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "CONTACT" page is opened')
    def assert_page_is_displayed(self):
        self.assert_page_title_and_url(self.title, self.page)
        self.assert_element_is_visible(self.CONTACT_US_BANNER)

    @allure.step('Assert "CONTACT" page elements are present')
    def assert_sections_are_present(self):
        self.assert_element_is_visible(self.CONTACT_US_BANNER), 'CONTACT_US_BANNER not displayed'
        self.assert_element_is_visible(self.CONTACT_US_SECTION), 'CONTACT_US_SECTION not displayed'
        self.assert_element_is_visible(self.FIND_US_SECTION), 'FIND_US_SECTION not displayed'

    @allure.step('Fill in "First Name" field')
    def fill_in_first_name_field(self):
        self.insert_text(self.customer_data[0], self.FIRST_NAME_FIELD)

    @allure.step('Fill in "Last Name" field')
    def fill_in_last_name_field(self):
        self.insert_text(self.customer_data[1], self.LAST_NAME_FIELD)

    @allure.step('Fill in "Email" field')
    def fill_in_email_field(self):
        self.insert_text(self.customer_data[2], self.EMAIL_FIELD)

    @allure.step('Fill in "Message" field')
    def fill_in_message_field(self):
        self.insert_text(self.customer_data[3], self.MESSAGE_FIELD)

    # DRAFT VERSION, METHOD NEEDS TO BE REWORKED
    @allure.step('Fill in and submit "Contact Us" form')
    def fill_in_contact_us_form(self):
        self.click_on(self.SUBMIT_BUTTON)
        time.sleep(10)
        self.fill_in_first_name_field()
        time.sleep(10)
        self.fill_in_last_name_field()
        time.sleep(10)
        self.fill_in_email_field()
        time.sleep(10)
        self.fill_in_message_field()
        time.sleep(10)
        self.click_on(self.SUBMIT_BUTTON)
        time.sleep(10)
