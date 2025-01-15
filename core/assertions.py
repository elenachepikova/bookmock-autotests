import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core import Actions


class Assertions(Actions):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Assert element {selector} is visible')
    def assert_element_is_visible(self, selector):
        element = self.get_element(selector)
        assert element.is_displayed(), f"Element {selector} is not visible"

    def assert_element_is_not_visible(self, selector):
        invisibility = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(selector))
        assert invisibility == True, f"Element {selector} is visible"

    @allure.step('Assert element {selector} is selected')
    def assert_element_is_selected(self, selector):
        element = self.get_element(selector)
        assert element.is_selected(), f"Element {selector} is not selected"

    @allure.step('Assert element {selector} is active')
    def assert_element_is_active(self, selector):
        element = self.get_element(selector)
        assert "active" in element.get_attribute("class"), f"Expected element to be active, but it is not."

    @allure.step('Assert page title and URL')
    def assert_page_title_and_url(self, title, url):
        if title is not None:
            assert self.driver.title == title, f"Title should be {title}, but is {self.driver.title}"
        if url is not None:
            assert self.driver.current_url == url, f"Url should be {url}, but is {self.driver.current_url}"
