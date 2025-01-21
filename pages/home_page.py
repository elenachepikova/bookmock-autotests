import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Actions, Assertions
from data import DOMAIN, TITLE


class HomePage(Actions):
    BANNER = (By.ID, 'bb-section-512921E4-B305-83EC-0A36-1A624B3CBBFA')
    FEATURED_SECTION = (By.ID, 'bb-section-512921E5-B3EE-81BE-E747-F1A82516138D')
    RECENT_REVIEWS = (By.ID, 'bb-section-512921E6-02B3-DB71-72CB-05545E668750')
    SEARCH_AND_FILTER_BUTTON = (By.CSS_SELECTOR, '.d-block')
    PRODUCT = (By.ID, 'store-products-12463756')
    PRODUCTS = (By.CSS_SELECTOR, '.col-6.col-sm-6')
    SHOP_LINK = (By.CSS_SELECTOR, '.content-breadcrumbs a')
    harry_potter = f"{DOMAIN}/shop/product/untitled-product-2"
    twilight = f"{DOMAIN}/shop/product/untitled-product-1"
    nothing_found = 'No products matched your search criteria. Try widening your search.'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.page = f"{DOMAIN}/"
        self.title = TITLE
        self.assertions = Assertions(self.driver)

    @allure.step('Open Home page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "Home page" is opened')
    def assert_page_is_displayed(self):
        self.assertions.assert_page_title_and_url(self.title, self.page)
        self.assert_sections_are_present()

    @allure.step('Assert "HOME" page elements are present')
    def assert_sections_are_present(self):
        self.assertions.assert_element_is_visible(self.BANNER), 'BANNER not displayed'
        self.assertions.assert_element_is_visible(self.FEATURED_SECTION), 'FEATURED_SECTION not displayed'
        self.assertions.assert_element_is_visible(self.RECENT_REVIEWS), 'RECENT_REVIEWS not displayed'

    def click_on_search_and_filter_button(self):
        self.click_on(self.SEARCH_AND_FILTER_BUTTON)

    def assert_products_count(self, value):
        assert self.count_elements(self.PRODUCTS) == value, (f"Expected products count = {value}, "
                                                             f"actual = {self.count_elements(self.PRODUCTS)}")

    def assert_book_title(self, book_title):
        book = self.get_element(self.PRODUCT)
        assert self.get_book_title(book) == book_title

    def assert_first_book_title(self, book_title):
        first_book = self.return_first_element(self.PRODUCTS)
        assert self.get_book_title(first_book) == book_title

    def assert_no_results_found_message(self):
        self.assertions.assert_text(self.PRODUCT, self.nothing_found)

    def click_on_shop_link(self):
        self.click_on(self.SHOP_LINK)
