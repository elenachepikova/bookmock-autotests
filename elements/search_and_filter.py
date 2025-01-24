import allure
from selenium.webdriver.common.by import By

from core import Assertions


class SearchAndFilter(Assertions):
    SEARCH_AND_FILTER = (By.CSS_SELECTOR, '.products-filter-panel.show')
    TITLE = (By.CSS_SELECTOR, '.mb-0.bb-font-h5')
    CLOSE_ICON = (By.CSS_SELECTOR, '.close')
    SEARCH_FILED = (By.XPATH, '(//input[@name="search"])[2]')
    FICTION_CHECKBOX = (By.ID, 'related-12463756-CE90C2D4-7D05-93F8-041C-69F83F445526-panel')
    POPULAR_CHECKBOX = (By.ID, 'related-12463756-989E66B3-3ABA-A088-80F2-2DCBA7AE1641-panel')
    PRICE_MIN_FIELD = (By.XPATH, '(//*[contains(@class,"min-price")])[2]')
    PRICE_MAX_FIELD = (By.XPATH, '(//*[contains(@class,"max-price")])[2]')
    CLEAR_FILTER_BUTTON = (By.CSS_SELECTOR, '.clear-filter')
    APPLY_BUTTON = (By.CSS_SELECTOR, '.apply-filter')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Assert Cart sidebar is opened')
    def assert_search_and_filter_sidebar_is_displayed(self):
        self.assert_element_is_visible(self.SEARCH_AND_FILTER)
        self.assert_element_is_visible(self.TITLE)
        self.assert_element_is_visible(self.CLOSE_ICON)
        self.assert_element_is_visible(self.SEARCH_FILED)
        self.assert_element_is_visible(self.FICTION_CHECKBOX)
        self.assert_element_is_visible(self.POPULAR_CHECKBOX)
        self.assert_element_is_visible(self.PRICE_MIN_FIELD)
        self.assert_element_is_visible(self.PRICE_MAX_FIELD)
        self.assert_element_is_visible(self.CLEAR_FILTER_BUTTON)
        self.assert_element_is_visible(self.APPLY_BUTTON)
        self.assert_price_min_field_value("18")
        self.assert_price_max_field_value("25")

    @allure.step('Close "Search and Filter" sidebar by click on close icon')
    def click_on_close_icon(self):
        self.click_on(self.CLOSE_ICON)

    @allure.step('Click on "Apply" button on "Search and Filter" sidebar')
    def click_on_apply_button(self):
        self.click_on(self.APPLY_BUTTON)
        self.assert_search_and_filter_sidebar_is_not_displayed()

    @allure.step('Click on "Clear Filter" button on "Search and Filter" sidebar')
    def click_on_clear_filter_button(self):
        self.click_on(self.CLEAR_FILTER_BUTTON)
        self.assert_search_and_filter_sidebar_is_not_displayed()

    @allure.step('Check "Popular" checkbox in "Collections" section on "Search and Filter" sidebar')
    def check_popular_checkbox(self):
        self.click_on(self.POPULAR_CHECKBOX)

    @allure.step('Check "Fiction" checkbox in "Collections" section on "Search and Filter" sidebar')
    def check_fiction_checkbox(self):
        self.click_on(self.FICTION_CHECKBOX)

    @allure.step('Assert "Search and Filter" sidebar is not displayed')
    def assert_search_and_filter_sidebar_is_not_displayed(self):
        self.wait_for_element_invisibility(self.SEARCH_AND_FILTER), ("'Search and Filter' "
                                                                     "sidebar is still visible!")

    @allure.step('Enter {value} into "Search" field on "Search and Filter" sidebar')
    def fill_in_search_field(self, value):
        self.insert_text(value, self.SEARCH_FILED)

    @allure.step('Clear "Search" field on "Search and Filter" sidebar')
    def clear_search_field(self):
        self.clear_text(self.SEARCH_FILED)

    @allure.step('Enter {value} into min Price field on "Search and Filter" sidebar')
    def fill_in_price_min_field(self, value):
        self.clear_text(self.PRICE_MIN_FIELD)
        self.insert_text(value, self.PRICE_MIN_FIELD)

    @allure.step('Enter {value} into max Price field on "Search and Filter" sidebar')
    def fill_in_price_max_field(self, value):
        self.clear_text(self.PRICE_MAX_FIELD)
        self.insert_text(value, self.PRICE_MAX_FIELD)

    @allure.step('Assert min Price value on "Search and Filter" sidebar')
    def assert_price_min_field_value(self, value):
        self.assert_value(self.PRICE_MIN_FIELD, value)

    @allure.step('Assert max Price value on "Search and Filter" sidebar')
    def assert_price_max_field_value(self, value):
        self.assert_value(self.PRICE_MAX_FIELD, value)
