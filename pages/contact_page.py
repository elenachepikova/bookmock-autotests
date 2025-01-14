import time
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Actions, Assertions
from data import DOMAIN, TITLE
from data.customer_db_usage import get_customer_from_db


class ContactPage(Actions):
    CONTACT_US_BANNER = (By.ID, 'bb-section-51292A57-9603-A922-BC8E-363F9F372AE4')
    CONTACT_US_SECTION = (By.ID, 'bb-section-51292A58-BF7C-41C2-A137-AA892D924926')
    FIND_US_SECTION = (By.ID, 'bb-section-51292A59-E3FC-802D-398A-7CA900B7C05F')
    FIRST_NAME_FIELD = (By.XPATH, '//*[@name="First Name"]')
    LAST_NAME_FIELD = (By.XPATH, '//*[@name="Last Name"]')
    EMAIL_FIELD = (By.XPATH, '//*[@name="Email"]')
    MESSAGE_FIELD = (By.XPATH, '//*[@name="Message"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary')
    customer_data = get_customer_from_db()
    first_name = customer_data[0]
    last_name = customer_data[1]
    email = customer_data[2]
    message = customer_data[3]


    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f'{DOMAIN}contact'
        self.title = f'CONTACT | {TITLE}'
        self.assertions = Assertions(self.driver)

    @allure.step('Open CONTACT page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "CONTACT" page is opened')
    def assert_page_is_displayed(self):
        self.assertions.assert_page_title_and_url(self.title, self.page)
        self.assertions.assert_element_is_visible(self.CONTACT_US_BANNER)

    @allure.step('Assert "CONTACT" page elements are present')
    def assert_sections_are_present(self):
        self.assertions.assert_element_is_visible(self.CONTACT_US_BANNER), 'CONTACT_US_BANNER not displayed'
        self.assertions.assert_element_is_visible(self.CONTACT_US_SECTION), 'CONTACT_US_SECTION not displayed'
        self.assertions.assert_element_is_visible(self.FIND_US_SECTION), 'FIND_US_SECTION not displayed'

    @allure.step('Fill in "First Name" field')
    def fill_in_first_name_field(self):
        self.input_text(self.first_name, self.FIRST_NAME_FIELD)
        # assert self.get_attribute(self.FIRST_NAME_FIELD) == False, 'FIRST_NAME_FIELD aria-invalid="true"'

    @allure.step('Fill in "Last Name" field')
    def fill_in_last_name_field(self):
        self.input_text(self.last_name, self.LAST_NAME_FIELD)
        # assert self.get_attribute(self.LAST_NAME_FIELD) == False, 'LAST_NAME_FIELD aria-invalid="true"'

    @allure.step('Fill in "Email" field')
    def fill_in_email_field(self):
        self.input_text(self.email, self.EMAIL_FIELD)
        # assert self.get_attribute(self.EMAIL_FIELD) == False, 'EMAIL_FIELD aria-invalid="true"'

    @allure.step('Fill in "Message" field')
    def fill_in_message_field(self):
        self.input_text(self.message, self.MESSAGE_FIELD)
        # assert self.get_attribute(self.MESSAGE_FIELD) == False, 'MESSAGE_FIELD aria-invalid="true"'

    @allure.step('Fill in and submit "Contact Us" form')
    def fill_in_contact_us_form(self):
        self.click_on(self.SUBMIT_BUTTON)
        time.sleep(10)
        self.fill_in_first_name_field()
        self.fill_in_last_name_field()
        self.fill_in_email_field()
        self.fill_in_message_field()
        time.sleep(10)
        self.click_on(self.SUBMIT_BUTTON)
        time.sleep(30)