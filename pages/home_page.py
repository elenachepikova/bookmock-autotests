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
    PRODUCTS = (By.CSS_SELECTOR, '.col-6.col-sm-6')

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
