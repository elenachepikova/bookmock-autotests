import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

    @allure.step('Get href value for child attribute based on parent selector')
    def get_link_attribute(self, selector):
        parent_element = self.get_element(selector)
        element = parent_element.find_element(By.XPATH, ".//a")
        link = element.get_attribute("href")
        return link

    @allure.step('Count the number of elements found by selector')
    def count_elements(self, selector):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(selector))
        return len(elements)

    @allure.step('Find the first of all elements found by selector')
    def return_first_element(self, selector):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(selector))
        return elements[0]

    @allure.step('Select item from drop-down')
    def select_dropdown_option(self, selector, value):
        select = Select(self.get_element(selector))
        return select.select_by_value(value)

    @allure.step('Get book title')
    def get_book_title(self, book):
        title = book.find_element(By.XPATH, ".//h5").text
        return title

    @allure.step('Wait until item is NOT displayed')
    def wait_for_item_invisibility(self, selector):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(selector))
