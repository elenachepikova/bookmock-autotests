import allure
from selenium.webdriver.common.by import By

from core import Assertions


class NavigationPanel(Assertions):
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

    @allure.step('Assert header navigation panel items presence')
    def assert_header_is_displayed(self):
        self.assert_element_is_visible(self.HEADER), f"HEADER not displayed"
        self.assert_element_is_visible(self.LOGO), f"LOGO icon not displayed"
        self.assert_element_is_visible(self.HOME), f"HOME button not displayed"
        self.assert_element_is_visible(self.ABOUT), f"ABOUT button not displayed"
        self.assert_element_is_visible(self.SHOP), f"SHOP button not displayed"
        self.assert_element_is_visible(self.FAQ), f"FAQ button not displayed"
        self.assert_element_is_visible(self.CONTACT), f"CONTACT button not displayed"
        self.assert_element_is_visible(self.SHOP_NOW), f"SHOP_NOW button not displayed"
        self.assert_element_is_visible(self.CART), f"CART icon not displayed"

    @allure.step('Click on logo icon in navigation panel')
    def click_on_logo(self):
        self.click_on(self.LOGO)

    @allure.step('Click on HOME button in navigation panel')
    def click_on_home_item(self):
        self.click_on(self.HOME)

    @allure.step('Click on ABOUT button in navigation panel')
    def click_on_about_item(self):
        self.click_on(self.ABOUT)

    @allure.step('Click on SHOP button in navigation panel')
    def click_on_shop_item(self):
        self.click_on(self.SHOP)

    @allure.step('Click on FAQ button in navigation panel')
    def click_on_faq_item(self):
        self.click_on(self.FAQ)

    @allure.step('Click on CONTACT button in navigation panel')
    def click_on_contact_item(self):
        self.click_on(self.CONTACT)

    @allure.step('Click on SHOP NOW button in navigation panel')
    def click_on_shop_now_button(self):
        self.click_on(self.SHOP_NOW)

    @allure.step('Click on CART icon in navigation panel')
    def click_on_cart_icon(self):
        self.click_on(self.CART)
