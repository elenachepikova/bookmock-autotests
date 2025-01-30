import allure
from selenium.webdriver.common.by import By

from core import ProductActions
from data import DOMAIN, TITLE


class ProductPage(ProductActions):
    NAVIGATION_SECTION = (By.CSS_SELECTOR, "nav.d-flex.mb-4")

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    @allure.step("Generate product page url based on given path")
    def get_page_url(path):
        page = f"{DOMAIN}/shop/product/{path}"
        return page

    @staticmethod
    @allure.step("Generate product page url based on given product title")
    def get_page_title(book_title):
        title = f"{book_title} | {TITLE}"
        return title

    @allure.step('Assert "Product" is opened')
    def assert_page_is_displayed(self, book_title, path):
        expected_url = self.get_page_url(path)
        expected_title = self.get_page_title(book_title)

        self.assert_page_title_and_url(expected_title, expected_url)
        self.assert_element_is_visible(self.PRODUCT_NAME)
        self.assert_text(self.PRODUCT_NAME, book_title)

    @allure.step("Open Product page")
    def open(self, path):
        page = self.get_page_url(path)
        self.driver.get(page)

    @allure.step("Assert Product page UI")
    def assert_product_page_ui(self):
        self.assert_element_is_visible(self.NAVIGATION_SECTION)
        self.assert_product_elements()
