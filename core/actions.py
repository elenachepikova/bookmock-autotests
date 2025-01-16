import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Actions:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    @allure.step('Find element by selector')
    def get_element(self, selector):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
        return element

    @allure.step('Click_on {selector}')
    def click_on(self, selector, force=False):
        element = self.get_element(selector)
        if force:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step('Fill in the field with {text}')
    def input_text(self, text, selector):
        field = self.get_element(selector)
        field.send_keys(text)

    @allure.step('Clear text field')
    def clear_text(self, selector):
        field = self.get_element(selector)
        field.clear()
        assert field.get_attribute("value") == ''
