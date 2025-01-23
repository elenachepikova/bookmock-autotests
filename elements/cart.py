import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Assertions


class Cart(Assertions):
    CART = (By.CSS_SELECTOR, '.bb-cart.show')
    TITLE = (By.CSS_SELECTOR, '.mb-0.bb-font-h5')
    CLOSE_ICON = (By.XPATH, '//*[@aria-label="Close Sidebar"]')
    MESSAGE = (By.CSS_SELECTOR, '.text-center.mt-5>.bb-font-h5')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, 'button.btn.mt-4')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.message = self.wait_for_element(self.MESSAGE)

    @allure.step('Assert Cart sidebar is opened')
    def assert_cart_sidebar_is_displayed(self):
        self.assert_element_is_visible(self.CART)
        self.assert_element_is_visible(self.TITLE)
        self.assert_element_is_visible(self.CLOSE_ICON)

    @allure.step('Assert Cart sidebar is opened in empty state')
    def assert_empty_cart_is_displayed(self):
        self.assert_cart_sidebar_is_displayed()
        self.assert_element_is_visible(self.MESSAGE)
        assert self.message.text == 'Your Cart is Empty'
        self.assert_element_is_visible(self.CONTINUE_SHOPPING_BUTTON)

    @allure.step('Assert Cart sidebar is not displayed')
    def assert_cart_is_not_displayed(self):
        self.wait_for_element_invisibility(self.CART), "Cart sidebar is still visible!"

    @allure.step('Close Cart sidebar by click on close icon')
    def click_on_close_icon(self):
        self.click_on(self.CLOSE_ICON)
