import allure

from core import BaseActions


class Assertions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Assert element {selector} is visible')
    def assert_element_is_visible(self, selector):
        element = self.wait_for_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"

    @allure.step('Assert page title and URL')
    def assert_page_title_and_url(self, title, url):
        if title is not None:
            assert self.driver.title == title, f"Title should be {title}, but is {self.driver.title}"
        if url is not None:
            assert self.driver.current_url == url, f"Url should be {url}, but is {self.driver.current_url}"

    def assert_text(self, selector, text):
        element = self.wait_for_element(selector)
        assert element.text == text, f'Text for {element} is not found'

    def assert_value(self, selector, expected_value):
        element = self.wait_for_element(selector)
        actual_value = element.get_attribute("value")
        assert actual_value == expected_value, (f'Expected value for {selector}: '
                                                f'{expected_value}, actual - {actual_value}')
