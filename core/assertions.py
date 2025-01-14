import allure

from core.actions import Actions


class Assertions(Actions):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Assert element {selector} is visible')
    def assert_element_is_visible(self, selector):
        element = self.get_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"

    @allure.step('Assert element {selector} is selected')
    def assert_element_is_selected(self, selector):
        element = self.get_element(selector)
        assert element.is_selected(), f"Element {selector} is not selected"

    @allure.step('Assert element {selector} is active')
    def assert_element_is_active(self, selector):
        element = self.get_element(selector)
        assert "active" in element.get_attribute("class"), f"Expected element to be active, but it is not."

    @allure.step('Assert page title')
    def assert_page_title(self, title):
        assert self.driver.title == title

    @allure.step('Assert page URL')
    def assert_page_url(self, url):
        assert self.driver.current_url == url, f"Url should be {url}, but is {self.driver.current_url}"
