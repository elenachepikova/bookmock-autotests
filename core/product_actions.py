import allure
from selenium.webdriver.common.by import By

from core import CommonActions


class ProductActions(CommonActions):
    PRODUCT_NAME = (By.CSS_SELECTOR, '.bb-product-name')
    FINAL_PRICE = (By.CSS_SELECTOR, '.bb-product-final-price')
    ORIGINAL_PRICE = (By.CSS_SELECTOR, '.bb-product-original-price')
    QUANTITY_FIELD = (By.NAME, 'bb-product-qty')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.bb-store-add-product')
    DESCRIPTION_SECTION = (By.CSS_SELECTOR, 'div.mt-5')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '.product-image')
    PRODUCT_PREVIEW = (By.CSS_SELECTOR, '.product-thumbnail-image')
    COVER_SELECTOR = (By.NAME, 'bb-options-Cover')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Assert Product related elements presence')
    def assert_product_elements(self):
        self.assert_element_is_visible(self.PRODUCT_IMAGE), 'PRODUCT_IMAGE not displayed'
        self.assert_element_is_visible(self.FINAL_PRICE), 'FINAL_PRICE not displayed'
        self.assert_element_is_visible(self.QUANTITY_FIELD), 'QUANTITY_FIELD not displayed'
        self.assert_element_is_visible(self.ADD_TO_CART_BUTTON), 'ADD_TO_CART_BUTTON not displayed'
        self.assert_element_is_visible(self.DESCRIPTION_SECTION), 'DESCRIPTION_SECTION not displayed'
        self.assert_element_is_visible(self.PRODUCT_PREVIEW), 'PRODUCT_PREVIEW not displayed'
        assert self.get_label(self.DESCRIPTION_SECTION) == "Description", "DESCRIPTION title is not 'Description'"
        assert self.get_label(self.ADD_TO_CART_BUTTON) == "Add to Cart", "Invalid name of 'Add to Cart' button"
        self.assert_value(self.QUANTITY_FIELD, "1"), 'QUANTITY_FIELD value != 1'

    @allure.step('Assert original price is present for discounted product')
    def assert_original_price_presence(self):
        self.assert_element_is_visible(self.ORIGINAL_PRICE), 'ORIGINAL_PRICE is not displayed'

    @allure.step('Assert original price is NOT present for regular product')
    def assert_original_price_absence(self):
        self.assert_element_absense(self.ORIGINAL_PRICE), 'ORIGINAL_PRICE is displayed'

    @allure.step('Assert cover selector is present for product with cover options')
    def assert_cover_selector_presence(self):
        self.assert_element_is_visible(self.COVER_SELECTOR), 'COVER_SELECTOR is not displayed'

    @allure.step('Assert cover selector is NOT present for regular product')
    def assert_cover_selector_absence(self):
        self.assert_element_absense(self.COVER_SELECTOR), 'COVER_SELECTOR is displayed'

    @allure.step('Select "Hard" option in Cover drop-down')
    def select_hard_cover(self):
        self.select_dropdown_option(self.COVER_SELECTOR, "A")

    @allure.step('Select "Soft" option in Cover drop-down')
    def select_soft_cover(self):
        self.select_dropdown_option(self.COVER_SELECTOR, "B")

    @allure.step('Set {value} value in Quantity field')
    def set_quantity(self, value):
        self.clear_text(self.QUANTITY_FIELD)
        self.insert_text(value, self.QUANTITY_FIELD)
