import allure
from selenium.webdriver.common.by import By

from core import Assertions
from data import NOT_FOUND_MESSAGE


class CommonActions(Assertions):
    SPINNER = (By.CSS_SELECTOR, ".loading-overlay")
    PRODUCT = (By.CSS_SELECTOR, '.store-products')
    PRODUCTS = (By.CSS_SELECTOR, '.col-6.col-sm-6')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.search-results')
    SHOP_LINK = (By.CSS_SELECTOR, '.content-breadcrumbs a')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.sm-add-to-cart')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Get the title of the first product in the range')
    def get_first_book_title(self, selector):
        first_book = self.return_first_element(selector)
        first_book_title = first_book.find_element(By.XPATH, ".//h5").text
        return first_book_title

    @allure.step('Assert product title corresponds to expected {expected_title}')
    def assert_first_book_title(self, expected_title):
        actual_title = self.get_first_book_title(self.PRODUCTS)
        assert actual_title == expected_title, f"Expected product title - {expected_title}, actual - {actual_title}"

    @allure.step('Wait for page to load')
    def wait_for_page_to_load(self):
        self.wait_for_element_invisibility(self.SPINNER)

    @allure.step('Assert valid message if displayed if no results matches search criteria')
    def assert_no_results_found_message(self):
        self.assert_text(self.PRODUCT, NOT_FOUND_MESSAGE)

    @allure.step('Assert elements count is {value}')
    def assert_products_count(self, value):
        assert self.count_elements(self.PRODUCTS) == value, (f"Expected products count = {value}, "
                                                             f"actual = {self.count_elements(self.PRODUCTS)}")
        self.assert_text(self.SEARCH_RESULTS, f"Showing 1-{value} of {value} results")

    @allure.step('Check checkbox and wait for page to load')
    def check_checkbox(self, selector):
        self.click_on(selector)
        self.wait_for_page_to_load()

    @allure.step('Click on "SHOP" link')
    def click_on_shop_link(self):
        self.click_on(self.SHOP_LINK)

    @allure.step('Sort products by dropdown value {value} and wait for page to load')
    def sort_by_value(self, selector, value):
        self.select_dropdown_option(selector, value)
        self.wait_for_page_to_load()

    @allure.step('Click on product link')
    def click_on_product_link(self):
        self.click_on(self.PRODUCTS)

    @allure.step('Click on "Add to Cart" button')
    def click_on_add_to_cart_button(self):
        self.click_on(self.ADD_TO_CART_BUTTON)
