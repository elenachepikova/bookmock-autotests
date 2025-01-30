import allure
from selenium.webdriver.common.by import By

from core import CommonActions


class CheckoutPage(CommonActions):
    CHECKOUT_TITLE = (By.ID, "checkout-header-title")
    SUB_HEADER_1 = (By.XPATH, '(//*[@class="hp-card-header"]/h4)[1]')
    SUB_HEADER_2 = (By.XPATH, '(//*[@class="hp-card-header"]/h4)[2]')
    EMAIL_FIELD = (By.ID, "checkout-email")
    FIRST_NAME_FIELD = (By.ID, "checkout-firstName")
    LAST_NAME_FIELD = (By.ID, "checkout-lastName")
    ADDRESS_FIELD_1 = (By.ID, "checkout-addressLine1")
    ADDRESS_FIELD_2 = (By.ID, "checkout-addressLine2")
    CITY_FIELD = (By.ID, "checkout-city")
    POSTAL_CODE_FIELD = (By.ID, "checkout-postalCode")
    COUNTRY_SELECTOR = (By.ID, "checkout-country")
    STATE_SELECTOR = (By.ID, "checkout-state")
    PHONE_FIELD = (By.ID, "checkout-phone")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button.checkout-continue")
    SUBMIT_BUTTON = (By.ID, "offline-payment-btn")
    THANK_YOU_CARD = (By.XPATH, '(//*[@class="thank-you-subheader"])[1]')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, ".hp-btn-primary")

    def __init__(self, driver, customer_data=None):
        super().__init__(driver)
        self.page = (
            "https://checkout-qmrd57hz.websiteserver4.com/_storeManager.checkout"
        )
        self.title = "SimulateCo - Secure Checkout"
        self.customer_data = customer_data

    @allure.step("Assert Customer Details checkout step is opened")
    def assert_customer_info_step_opened(self):
        self.assert_page_title_and_url(self.title, self.page)
        self.assert_text(self.CHECKOUT_TITLE, "SimulateCo")
        self.assert_text(self.SUB_HEADER_1, "Contact Information")
        self.assert_text(self.SUB_HEADER_2, "Customer Address")
        self.assert_text(self.CONTINUE_BUTTON, "Continue to Shipping")

    @allure.step("Assert Shipping Details checkout step is opened")
    def assert_shipping_details_step_opened(self):
        self.assert_page_title_and_url(self.title, self.page)
        self.assert_text(self.CHECKOUT_TITLE, "SimulateCo")
        self.assert_label(self.SUB_HEADER_1, "Customer Address")
        self.assert_label(self.SUB_HEADER_2, "Shipping Method")
        self.assert_text(self.CONTINUE_BUTTON, "Continue to Payment")

    @allure.step("Assert Shipping Details checkout step is opened")
    def assert_payment_details_step_opened(self):
        self.assert_page_title_and_url(self.title, self.page)
        self.assert_text(self.CHECKOUT_TITLE, "SimulateCo")
        self.assert_label(self.SUB_HEADER_1, "Payment")
        self.assert_text(self.SUBMIT_BUTTON, "Submit")

    @allure.step("Assert Purchase Completed checkout step is opened")
    def assert_thank_you_step_opened(self):
        self.assert_page_title_and_url(self.title)
        self.assert_text(self.CHECKOUT_TITLE, "SimulateCo")
        self.assert_label(self.THANK_YOU_CARD, "Your order is being processed!")

    def click_on_continue_button(self):
        self.click_on(self.CONTINUE_BUTTON)
        self.wait_for_page_to_load()

    def click_on_submit_button(self):
        self.click_on(self.SUBMIT_BUTTON)
        self.wait_for_page_to_load()

    def select_country(self):
        self.select_dropdown_option(self.COUNTRY_SELECTOR, self.customer_data[5])

    def select_state(self):
        self.select_dropdown_option(self.STATE_SELECTOR, self.customer_data[6])

    @allure.step('Fill in and submit "Checkout" form')
    def fill_in_checkout_form(self):
        self.insert_text(self.customer_data[2], self.EMAIL_FIELD)
        self.insert_text(self.customer_data[0], self.FIRST_NAME_FIELD)
        self.insert_text(self.customer_data[1], self.LAST_NAME_FIELD)
        self.insert_text(self.customer_data[3], self.ADDRESS_FIELD_1)
        self.insert_text(self.customer_data[4], self.CITY_FIELD)
        self.insert_text(self.customer_data[7], self.PHONE_FIELD)
        self.select_country()
        self.select_state()
        self.click_on_continue_button()
