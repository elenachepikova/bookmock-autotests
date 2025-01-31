import allure
from selenium.webdriver.common.by import By

from core import Assertions
from data import DOMAIN, TITLE


class AboutPage(Assertions):
    ABOUT_US_BANNER = (By.ID, "bb-section-5129237E-F62C-D51F-8FF0-2BFF121EE5F7")
    CONTACT_US = (By.XPATH, '//button[contains(text(),"CONTACT US")]')
    SHOP_NOW = (By.CSS_SELECTOR, "button.btn-secondary")
    WELCOME_SECTION = (By.ID, "bb-section-5129237F-D43A-8412-5DD5-6C3DF38BD7AE")
    OUR_MISSION_SECTION = (By.ID, "bb-section-51292380-E3AF-AFFB-A3B9-46FBDB6E6D1F")
    OUR_VISION_SECTION = (By.ID, "bb-section-51292381-DA48-BCB9-9163-D3E6ED65874B")
    GALLERY = (By.ID, "bb-section-51292382-DFB4-576E-4DE7-7EB42AD3A4F6")
    PICTURE = (By.CSS_SELECTOR, ".gallery-media-wrapper")

    def __init__(self, driver):
        super().__init__(driver)
        self.page = f"{DOMAIN}/about"
        self.title = f"ABOUT | {TITLE}"

    @allure.step("Open About page")
    def open(self):
        self.driver.get(self.page)

    @allure.step('Assert "About" page is opened')
    def assert_page_is_displayed(self):
        self.assert_page_title_and_url(self.title, self.page)
        self.assert_element_is_visible(self.ABOUT_US_BANNER)
        self.assert_banner_title("ABOUT US")

    @allure.step('Assert "About" page UI')
    def assert_about_page_ui(self):
        self.assert_page_is_displayed()
        self.assert_element_is_visible(self.WELCOME_SECTION)
        self.assert_element_is_visible(self.OUR_MISSION_SECTION)
        self.assert_element_is_visible(self.OUR_VISION_SECTION)
        self.assert_element_is_visible(self.GALLERY)
        self.assert_label(self.WELCOME_SECTION, "Welcome to BookMock!")
        self.assert_label(self.OUR_MISSION_SECTION, "Our Mission")
        self.assert_label(self.OUR_VISION_SECTION, "Our Vision")
        assert self.count_elements(self.PICTURE) == 6, "PICTURE count != 6"

    @allure.step('Click on "CONTACT US" button on ABOUT page')
    def click_on_contact_us_button(self):
        self.click_on(self.CONTACT_US)

    @allure.step('Click on "SHOP NOW" button on ABOUT page')
    def click_on_shop_now_button(self):
        self.click_on(self.SHOP_NOW)
