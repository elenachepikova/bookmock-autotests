import allure
from selenium.webdriver.common.by import By

from core import BaseActions


class Assertions(BaseActions):
    BANNER_TITLE = (By.XPATH, '//*[@class=" bb-font-h2"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Assert element {selector} is visible")
    def assert_element_is_visible(self, selector):
        element = self.wait_for_element(selector)
        assert element.is_displayed(), f"Element {selector[1]} is not visible"

    @allure.step("Assert element {selector} is not present")
    def assert_element_absense(self, selector):
        elements = self.driver.find_elements(*selector)
        assert len(elements) == 0, f"Unexpected element(s) {selector} present on page"

    @allure.step("Assert page title and URL")
    def assert_page_title_and_url(self, title=None, url=None):
        if title is not None:
            assert self.driver.title == title, (
                f"Title should be {title}, " f"but is {self.driver.title}"
            )
        if url is not None:
            assert self.driver.current_url == url, (
                f"Url should be {url}, " f"but is {self.driver.current_url}"
            )

    @allure.step("Assert {selector} field contains text {text}")
    def assert_text(self, selector, text):
        element = self.wait_for_element(selector)
        assert element.text == text, (
            f"Expected text: {text}, " f"actual: {element.text}"
        )

    @allure.step("Assert {selector} label contains text {text}")
    def assert_label(self, selector, text):
        actual_text = self.get_label(selector)
        assert actual_text == text, f"Expected text: {text}, " f"actual: {actual_text}"

    @allure.step("Assert page main banner contains text {text}")
    def assert_banner_title(self, text):
        self.assert_text(self.BANNER_TITLE, text), f"Banner text is not {text}"

    @allure.step("Assert {selector} field contains value {expected_value}")
    def assert_value(self, selector, expected_value):
        element = self.wait_for_element(selector)
        actual_value = element.get_attribute("value")
        assert actual_value == expected_value, (
            f"Expected value for {selector}: "
            f"{expected_value}, actual - {actual_value}"
        )
