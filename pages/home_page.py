import allure
from selenium.webdriver.common.by import By

from core import CommonActions
from data import DOMAIN, TITLE


class HomePage(CommonActions):
    BANNER = (By.ID, 'bb-section-512921E4-B305-83EC-0A36-1A624B3CBBFA')
    BANNER_NAME = "Welcome to BookMock!"
    FEATURED_SECTION = (By.ID, 'bb-section-512921E5-B3EE-81BE-E747-F1A82516138D')
    FEATURED_SECTION_TITLE = (By.XPATH, '//*[@class="bb-font-h2"]')
    RECENT_REVIEWS = (By.ID, 'bb-section-512921E6-02B3-DB71-72CB-05545E668750')
    RECENT_REVIEWS_TITLE = (By.XPATH, '//*[@class=" bb-font-h3"]')
    RECENT_REVIEWS_NAME = "RECENT REVIEWS"
    REVIEWS = (By.CSS_SELECTOR, '.col-12.col-md-6')
    SEARCH_AND_FILTER_BUTTON = (By.CSS_SELECTOR, '.d-block')

    def __init__(self, driver):
        super().__init__(driver)
        self.page = f"{DOMAIN}/"
        self.title = TITLE

    @allure.step('Open Home page')
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "Home page" is opened')
    def assert_page_is_displayed(self):
        self.assert_page_title_and_url(self.title, self.page)
        self.assert_element_is_visible(self.BANNER)
        self.assert_banner_title(self.BANNER_NAME)

    @allure.step('Assert "HOME" page elements are present')
    def assert_sections_are_present(self):
        self.assert_element_is_visible(self.BANNER), 'BANNER not displayed'
        self.assert_element_is_visible(self.FEATURED_SECTION), 'FEATURED_SECTION not displayed'
        self.assert_element_is_visible(self.RECENT_REVIEWS), 'RECENT_REVIEWS not displayed'
        self.assert_text(self.FEATURED_SECTION_TITLE, "Featured")
        self.assert_text(self.RECENT_REVIEWS_TITLE, "RECENT REVIEWS")
        assert self.count_elements(self.REVIEWS) == 2

    def click_on_search_and_filter_button(self):
        self.click_on(self.SEARCH_AND_FILTER_BUTTON)
