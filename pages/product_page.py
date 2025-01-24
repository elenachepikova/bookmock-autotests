import allure
from selenium.webdriver.common.by import By

from core import CommonActions
from data import DOMAIN, TITLE


class ProductPage(CommonActions):
    PRODUCT_NAME = (By.CSS_SELECTOR, '.bb-product-name')
    NAVIGATION_SECTION = (By.CSS_SELECTOR, 'nav.d-flex.mb-4')
    FINAL_PRICE = (By.CSS_SELECTOR, '.bb-product-final-price')
    ORIGINAL_PRICE = (By.CSS_SELECTOR, '.bb-product-original-price')
    QUANTITY_FIELD = (By.NAME, 'bb-product-qty')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.bb-store-add-product')
    DESCRIPTION_SECTION = (By.CSS_SELECTOR, 'div.mt-5')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '.product-image')
    PRODUCT_PREVIEW = (By.CSS_SELECTOR, '.product-thumbnail-image')
    COVER_SELECTOR = (By.NAME, 'bb-options-Cover')

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    @allure.step('Generate product page url based on given path')
    def get_page_url(path):
        page = f'{DOMAIN}/shop/product/{path}'
        return page

    @staticmethod
    @allure.step('Generate product page url based on given product title')
    def get_page_title(book_title):
        title = f'{book_title} | {TITLE}'
        return title

    @allure.step('Assert "Product" is opened')
    def assert_page_is_displayed(self, book_title, path):
        expected_url = self.get_page_url(path)
        expected_title = self.get_page_title(book_title)

        self.assert_page_title_and_url(expected_title, expected_url)
        self.assert_element_is_visible(self.PRODUCT_NAME)
        self.assert_text(self.PRODUCT_NAME, book_title)

    @allure.step('Open Product page')
    def open(self, path):
        page = self.get_page_url(path)
        self.driver.get(page)

    @allure.step('Assert Product page UI')
    def assert_product_page_ui(self):
        self.assert_element_is_visible(self.NAVIGATION_SECTION), 'NAVIGATION_SECTION not displayed'
        self.assert_element_is_visible(self.PRODUCT_IMAGE), 'PRODUCT_IMAGE not displayed'
        self.assert_element_is_visible(self.FINAL_PRICE), 'FINAL_PRICE not displayed'
        self.assert_element_is_visible(self.QUANTITY_FIELD), 'QUANTITY_FIELD not displayed'
        self.assert_element_is_visible(self.ADD_TO_CART_BUTTON), 'ADD_TO_CART_BUTTON not displayed'
        self.assert_element_is_visible(self.DESCRIPTION_SECTION), 'DESCRIPTION_SECTION not displayed'
        self.assert_element_is_visible(self.PRODUCT_PREVIEW), 'PRODUCT_PREVIEW not displayed'
        assert self.get_label(self.DESCRIPTION_SECTION) == "Description"
        assert self.get_label(self.ADD_TO_CART_BUTTON) == "Add to Cart"
        self.assert_value(self.QUANTITY_FIELD, "1")

    def assert_original_price_presence(self):
        self.assert_element_is_visible(self.ORIGINAL_PRICE), 'ORIGINAL_PRICE is not displayed'

    def assert_original_price_absence(self):
        self.assert_element_absense(self.ORIGINAL_PRICE), 'ORIGINAL_PRICE is displayed'

    def assert_cover_selector_presence(self):
        self.assert_element_is_visible(self.COVER_SELECTOR), 'ORIGINAL_PRICE is not displayed'

    def assert_cover_selector_absence(self):
        self.assert_element_absense(self.COVER_SELECTOR), 'ORIGINAL_PRICE is displayed'
