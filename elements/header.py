import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from core.actions import Actions
from core.assertions import Assertions


class NavigationPanel(Actions):
    HEADER = (By.ID, 'bb-header-spacing')
    LOGO = (By.CSS_SELECTOR, '.d-flex.align-items-center.flex-wrap.flex-sm-nowrap')
    HOME = (By.XPATH, '//*[@role="menuitem"][1]')
    ABOUT = (By.XPATH, '//*[@role="menuitem"][2]')
    SHOP = (By.XPATH, '//*[@role="menuitem"][3]')
    FAQ = (By.XPATH, '//*[@role="menuitem"][4]')
    CONTACT = (By.XPATH, '//*[@role="menuitem"][5]')
    SHOP_NOW = (By.LINK_TEXT, 'SHOP NOW')
    CART = (By.XPATH, '//*[@aria-label="Open Cart"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver: WebDriver = driver
        self.assertions = Assertions(self.driver)

    @allure.step('Assert that all header navigation panel items are visible')
    def assert_header_is_displayed(self):
        self.assertions.assert_element_is_visible(self.HEADER)
        self.assertions.assert_element_is_visible(self.LOGO)
        self.assertions.assert_element_is_visible(self.HOME)
        self.assertions.assert_element_is_visible(self.ABOUT)
        self.assertions.assert_element_is_visible(self.SHOP)
        self.assertions.assert_element_is_visible(self.FAQ)
        self.assertions.assert_element_is_visible(self.CONTACT)
        self.assertions.assert_element_is_visible(self.SHOP_NOW)
        self.assertions.assert_element_is_visible(self.CART)
