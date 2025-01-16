import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Actions, Assertions


class SearchAndFilter(Actions):
    SEARCH_AND_FILTER = (By.CSS_SELECTOR, '.products-filter-panel.show')
    TITLE = (By.CSS_SELECTOR, '.mb-0.bb-font-h5')
    CLOSE_ICON = (By.CSS_SELECTOR, '.close')
    SEARCH_FILED = (By.XPATH, '(//input[@name="search"])[2]')
    FICTION_CHECKBOX = (By.ID, 'related-12463756-CE90C2D4-7D05-93F8-041C-69F83F445526-panel')
    POPULAR_CHECKBOX = (By.ID, 'related-12463756-989E66B3-3ABA-A088-80F2-2DCBA7AE1641-panel')
    PRICE_FROM_FIELD = (By.XPATH, '(//*[contains(@class,"min-price")])[2]')
    PRICE_TO_FIELD = (By.XPATH, '(//*[contains(@class,"max-price")])[2]')
    CLEAR_FILTER_BUTTON = (By.CSS_SELECTOR, '.clear-filter')
    APPLY_BUTTON = (By.CSS_SELECTOR, '.apply-filter')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.assertions = Assertions(self.driver)

    @allure.step('Assert Cart sidebar is opened')
    def assert_search_and_filter_sidebar_is_displayed(self):
        self.assertions.assert_element_is_visible(self.SEARCH_AND_FILTER)
        self.assertions.assert_element_is_visible(self.TITLE)
        self.assertions.assert_element_is_visible(self.CLOSE_ICON)
        self.assertions.assert_element_is_visible(self.SEARCH_FILED)
        self.assertions.assert_element_is_visible(self.FICTION_CHECKBOX)
        self.assertions.assert_element_is_visible(self.POPULAR_CHECKBOX)
        self.assertions.assert_element_is_visible(self.PRICE_FROM_FIELD)
        self.assertions.assert_element_is_visible(self.PRICE_TO_FIELD)
        self.assertions.assert_element_is_visible(self.CLEAR_FILTER_BUTTON)
        self.assertions.assert_element_is_visible(self.APPLY_BUTTON)

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
        # add verification that field are in default state?
        self.assert_search_and_filter_sidebar_is_not_displayed()

    @allure.step('Check "Popular" checkbox in "Collections" section on "Search and Filter" sidebar')
    def check_popular_checkbox(self):
        self.click_on(self.POPULAR_CHECKBOX)

    @allure.step('Check "Fiction" checkbox in "Collections" section on "Search and Filter" sidebar')
    def check_fiction_checkbox(self):
        self.click_on(self.FICTION_CHECKBOX)

    @allure.step('Assert "Search and Filter" sidebar is not displayed')
    def assert_search_and_filter_sidebar_is_not_displayed(self):
        self.assertions.assert_element_is_not_visible(self.SEARCH_AND_FILTER), ("'Search and Filter' "
                                                                                "sidebar is still visible!")
