import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from core import Assertions


class CommonActions(Assertions):
    SPINNER = (By.CSS_SELECTOR, ".loading-overlay")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    def get_first_book_title(self, selector):
        first_book = self.return_first_element(selector)
        first_book_title = first_book.find_element(By.XPATH, ".//h5").text
        return first_book_title

    @allure.step('Wait for page to load')
    def wait_for_page_to_load(self):
        self.wait_for_element_invisibility(self.SPINNER)