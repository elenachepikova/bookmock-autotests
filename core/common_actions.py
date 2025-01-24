import allure
from selenium.webdriver.common.by import By

from core import Assertions
from data import NOT_FOUND_MESSAGE


class CommonActions(Assertions):
    SPINNER = (By.CSS_SELECTOR, ".loading-overlay")
    PRODUCT = (By.ID, 'store-products-12463756')
    PRODUCTS = (By.CSS_SELECTOR, '.col-6.col-sm-6')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.search-results')
    SHOP_LINK = (By.CSS_SELECTOR, '.content-breadcrumbs a')

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_book_title(self, selector):
        first_book = self.return_first_element(selector)
        first_book_title = first_book.find_element(By.XPATH, ".//h5").text
        return first_book_title

    def assert_first_book_title(self, book_title):
        assert self.get_first_book_title(self.PRODUCTS) == book_title

    @allure.step('Wait for page to load')
    def wait_for_page_to_load(self):
        self.wait_for_element_invisibility(self.SPINNER)

    def assert_no_results_found_message(self):
        self.assert_text(self.PRODUCT, NOT_FOUND_MESSAGE)

    def assert_products_count(self, value):
        assert self.count_elements(self.PRODUCTS) == value, (f"Expected products count = {value}, "
                                                             f"actual = {self.count_elements(self.PRODUCTS)}")
        self.assert_text(self.SEARCH_RESULTS, f"Showing 1-{value} of {value} results")

    def check_checkbox(self, selector):
        self.click_on(selector)
        self.wait_for_page_to_load()

    def click_on_shop_link(self):
        self.click_on(self.SHOP_LINK)

    def sort_by_value(self, selector, value):
        self.select_dropdown_option(selector, value)
        self.wait_for_page_to_load()