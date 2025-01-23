import allure
from selenium.webdriver.common.by import By

from core import CommonActions
from data import DOMAIN, TITLE


class ShopPage(CommonActions):
    ALL_PRODUCTS_TITLE = (By.CSS_SELECTOR, 'h2.bb-font-h2')
    SEARCH_SECTION = (By.XPATH, '(//*[@class="form-group"])[1]')
    SEARCH_FILED = (By.XPATH, '//input[@name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.search-btn')
    BROWSE_BY_SECTION = (By.XPATH, '(//*[@class="form-group"])[2]')
    COLLECTIONS_SECTION = (By.XPATH, '(//*[@class="form-group"])[3]')
    PRICE_SECTION = (By.XPATH, '(//*[@class="form-group"])[4]')
    SORT_BY_DROPDOWN = (By.CSS_SELECTOR, '.form-group.mb-0')
    PRODUCTS = (By.CSS_SELECTOR, '.col-6.col-sm-6')
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.search-results')
    PRICE_MIN_FIELD = (By.XPATH, '//*[contains(@class,"min-price")]')
    PRICE_MAX_FIELD = (By.XPATH, '//*[contains(@class,"max-price")]')
    FEATURED_CHECKBOX = (By.ID, 'related-12463765-FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF')
    ON_SALE_CHECKBOX = (By.ID, 'onSale-12463765')
    IN_STOCK_CHECKBOX = (By.ID, 'inStock-12463765')
    FICTION_CHECKBOX = (By.ID, 'related-12463765-CE90C2D4-7D05-93F8-041C-69F83F445526')
    NON_FICTION_CHECKBOX = (By.ID, 'related-12463765-A19E0E8F-7108-584C-E71F-0B41A6E2D90B')
    POPULAR_CHECKBOX = (By.ID, 'related-12463765-989E66B3-3ABA-A088-80F2-2DCBA7AE1641')

    def __init__(self, driver):
        super().__init__(driver)
        self.page = f'{DOMAIN}/shop'
        self.title = f'SHOP | {TITLE}'

    @allure.step('Open SHOP page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "SHOP" page is opened')
    def assert_page_is_displayed(self):
        self.assert_page_title_and_url(self.title, self.page)
        self.assert_element_is_visible(self.ALL_PRODUCTS_TITLE)
        self.assert_text(self.ALL_PRODUCTS_TITLE, "All Products")

    @allure.step('Assert All Products section UI')
    def assert_all_products_section_ui(self):
        self.assert_element_is_visible(self.SEARCH_SECTION), 'SEARCH_SECTION not displayed'
        self.assert_element_is_visible(self.BROWSE_BY_SECTION), 'BROWSE_BY_SECTION not displayed'
        self.assert_element_is_visible(self.COLLECTIONS_SECTION), 'COLLECTIONS_SECTION not displayed'
        self.assert_element_is_visible(self.PRICE_SECTION), 'PRICE_SECTION not displayed'
        self.assert_element_is_visible(self.SORT_BY_DROPDOWN), 'SORT_BY_DROPDOWN not displayed'
        assert self.get_label(self.SEARCH_SECTION) == "Search"
        assert self.get_label(self.BROWSE_BY_SECTION) == "Browse By"
        assert self.get_label(self.COLLECTIONS_SECTION) == "Collections:"
        assert self.get_label(self.PRICE_SECTION) == "Price ($):"
        self.assert_price_min_field_value("9")
        self.assert_price_max_field_value("25")

    def assert_products_count(self, value):
        assert self.count_elements(self.PRODUCTS) == value, (f"Expected products count = {value}, "
                                                             f"actual = {self.count_elements(self.PRODUCTS)}")
        self.assert_text(self.SEARCH_RESULTS, f"Showing 1-{value} of {value} results")

    @allure.step('Assert min Price value on "Search and Filter" sidebar')
    def assert_price_min_field_value(self, value):
        self.assert_value(self.PRICE_MIN_FIELD, value)

    @allure.step('Assert max Price value on "Search and Filter" sidebar')
    def assert_price_max_field_value(self, value):
        self.assert_value(self.PRICE_MAX_FIELD, value)

    def click_on_search_button(self):
        self.click_on(self.SEARCH_BUTTON)
        self.wait_for_page_to_load()

    @allure.step('Enter {value} into "Search" field on "SHOP" page')
    def fill_in_search_field(self, value):
        self.insert_text(value, self.SEARCH_FILED)

    def assert_first_book_title(self, book_title):
        assert self.get_first_book_title(self.PRODUCTS) == book_title

    @allure.step('Clear Filter on "SHOP" page')
    def clear_search_filter(self):
        self.clear_text(self.SEARCH_FILED)
        self.click_on_search_button()

    @allure.step('Check "Featured" checkbox in "Browse By" section on "SHOP" page')
    def check_featured_checkbox(self):
        self.click_on(self.FEATURED_CHECKBOX)
        self.wait_for_page_to_load()

    @allure.step('Check "On Sale" checkbox in "Browse By" section on "SHOP" page')
    def check_on_sale_checkbox(self):
        self.click_on(self.ON_SALE_CHECKBOX)
        self.wait_for_page_to_load()

    @allure.step('Check "In Stock" checkbox in "Browse By" section on "SHOP" page')
    def check_in_stock_checkbox(self):
        self.click_on(self.IN_STOCK_CHECKBOX)
        self.wait_for_page_to_load()

    @allure.step('Check "Fiction" checkbox in "Collections" section on "SHOP" page')
    def check_fiction_checkbox(self):
        self.click_on(self.FICTION_CHECKBOX)
        self.wait_for_page_to_load()

    @allure.step('Check "Non-fiction" checkbox in "Collections" section on "SHOP" page')
    def check_non_fiction_checkbox(self):
        self.click_on(self.NON_FICTION_CHECKBOX)
        self.wait_for_page_to_load()

    @allure.step('Check "Popular" checkbox in "Collections" section on "SHOP" page')
    def check_popular_checkbox(self):
        self.click_on(self.POPULAR_CHECKBOX)
        self.wait_for_page_to_load()

    @allure.step('Enter {value} into min Price field on "Search and Filter" sidebar')
    def fill_in_price_min_field(self, value):
        self.clear_price_min_field()
        self.insert_text(value, self.PRICE_MIN_FIELD)
        self.wait_for_page_to_load()

    @allure.step('Clear min Price field on "Search and Filter" sidebar')
    def clear_price_min_field(self):
        self.clear_text(self.PRICE_MIN_FIELD)

    @allure.step('Enter {value} into max Price field on "Search and Filter" sidebar')
    def fill_in_price_max_field(self, value):
        self.clear_price_max_field()
        self.insert_text(value, self.PRICE_MAX_FIELD)
        self.wait_for_page_to_load()

    @allure.step('Clear max Price field on "Search and Filter" sidebar')
    def clear_price_max_field(self):
        self.clear_text(self.PRICE_MAX_FIELD)
