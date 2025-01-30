import allure
from selenium.webdriver.common.by import By

from core import Assertions
from data import products


class Cart(Assertions):
    CART = (By.CSS_SELECTOR, ".bb-cart.show")
    TITLE = (By.CSS_SELECTOR, ".mb-0.bb-font-h5")
    CLOSE_ICON = (By.XPATH, '//*[@aria-label="Close Sidebar"]')
    MESSAGE = (By.CSS_SELECTOR, ".text-center.mt-5>.bb-font-h5")
    CART_ITEMS = (By.CSS_SELECTOR, ".bb-cart-items")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".d-block.bb-cart-product-name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".bb-cart-product-price")
    QUANTITY_SELECTOR = (By.NAME, "sm-cart-item-qty-1")
    CART_TOTAL = (By.CSS_SELECTOR, ".bb-cart-subtotal")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button.bb-cart-checkout-btn")
    CONTINUE_SHOPPING_BUTTON_E = (By.CSS_SELECTOR, "button.btn.mt-4")
    CONTINUE_SHOPPING_BUTTON_F = (By.CSS_SELECTOR, "button.bb-cart-continue-btn")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Assert Cart sidebar is opened")
    def assert_cart_sidebar_is_displayed(self):
        self.assert_element_is_visible(self.CART)
        self.assert_element_is_visible(self.TITLE)
        self.assert_element_is_visible(self.CLOSE_ICON)

    @allure.step("Assert Cart sidebar is opened in empty state")
    def assert_empty_cart_is_displayed(self):
        self.assert_cart_sidebar_is_displayed()
        self.assert_element_is_visible(self.MESSAGE)
        self.assert_text(self.MESSAGE, "Your Cart is Empty")
        self.assert_element_is_visible(self.CONTINUE_SHOPPING_BUTTON_E)

    @allure.step("Assert Cart sidebar is not displayed")
    def assert_cart_is_not_displayed(self):
        self.wait_for_element_invisibility(self.CART), "Cart sidebar is still visible!"

    @allure.step("Close Cart sidebar by click on close icon")
    def click_on_close_icon(self):
        self.click_on(self.CLOSE_ICON)

    @allure.step("Assert Cart sidebar is opened in empty state")
    def assert_cart_is_displayed(self):
        self.assert_cart_sidebar_is_displayed()
        self.assert_element_is_visible(self.CART_ITEMS)
        self.assert_element_is_visible(self.CART_TOTAL)
        self.assert_element_is_visible(self.CHECKOUT_BUTTON)
        self.assert_element_is_visible(self.CONTINUE_SHOPPING_BUTTON_F)

    @allure.step("Assert cart items count is {value}")
    def assert_cart_items_count(self, value):
        assert self.count_elements(self.PRODUCT_NAME) == value, (
            f"Expected items count = {value}, "
            f"actual = {self.count_elements(self.PRODUCT_NAME)}"
        )

    @allure.step("Assert cart item name is {title}")
    def assert_product_name(self, title):
        self.assert_text(self.PRODUCT_NAME, title)

    @allure.step("Assert cart item price is {value}")
    def assert_product_price(self, value):
        self.assert_text(self.PRODUCT_PRICE, value)

    @allure.step("Update quantity value for product in cart")
    def set_quantity(self, value: str):
        self.select_dropdown_option(self.QUANTITY_SELECTOR, value)

    @allure.step('Click on "Continue Shopping" button')
    def click_on_continue_shopping_button(self):
        self.click_on(self.CONTINUE_SHOPPING_BUTTON_F)

    @allure.step("Assert total price of all items in cart")
    def assert_cart_total(self):
        items_count = self.count_elements(self.PRODUCT_NAME)
        total = 0

        product_titles = self.wait_for_elements(self.PRODUCT_NAME)

        for i in range(items_count):
            title = product_titles[i].text
            qty = int(self.get_product_quantity(i))

            price = self.find_price_by_title(title)
            total += price * qty

        self.assert_text(self.CART_TOTAL, str(total))

    def get_product_quantity(self, index=0):
        dynamic_selector = (By.NAME, f"sm-cart-item-qty-{index + 1}")
        element = self.wait_for_element(dynamic_selector)
        value = element.get_attribute("data-current")
        return value

    @staticmethod
    def find_price_by_title(title):
        for product_key, product_info in products.items():
            if product_info["title"] == title:
                return float(product_info["price"])
