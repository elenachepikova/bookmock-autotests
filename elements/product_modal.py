import allure
from selenium.webdriver.common.by import By

from core import ProductActions


class ProductModal(ProductActions):
    CLOSE_ICON = (By.CSS_SELECTOR, '.close')


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Close Product modal by click on close icon')
    def click_on_close_icon(self):
        self.switch_to_default_content()
        self.click_on(self.CLOSE_ICON)
