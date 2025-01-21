import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core import Actions


class SortByDropdown(Actions):
    SORT_DROPDOWN = (By.CSS_SELECTOR, '[title="Sort Products"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver

    @allure.step('Sort products by Recently Added date')
    def sort_by_recently_added(self):
        self.select_dropdown_option(self.SORT_DROPDOWN, "createdDateDesc")

    @allure.step('Sort products by Price: from low to high')
    def sort_by_price_low_high(self):
        self.select_dropdown_option(self.SORT_DROPDOWN, "priceAsc")

    @allure.step('Sort products by Price: from high to low')
    def sort_by_price_high_low(self):
        self.select_dropdown_option(self.SORT_DROPDOWN, "priceDesc")

    @allure.step('Sort products by Name: from A to Z')
    def sort_by_name_a_z(self):
        self.select_dropdown_option(self.SORT_DROPDOWN, "nameAsc")

    @allure.step('Sort products by Name: from Z to A')
    def sort_by_name_z_a(self):
        self.select_dropdown_option(self.SORT_DROPDOWN, "nameDesc")
