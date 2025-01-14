import allure

from elements.header import NavigationPanel
from pages.about_page import AboutPage
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.shop_page import ShopPage


@allure.suite("Tests for 'ABOUT' page")
class TestAboutPage:

    @allure.title("Verify 'ABOUT' page is accessible via navigation panel")
    def test_open_about_page(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on(panel.ABOUT)
        about_page = AboutPage(driver)
        about_page.assert_page_is_displayed()

    @allure.title("Verify user is redirected from 'ABOUT' to 'CONTACT' via 'CONTACT US' button")
    def test_click_contact_us_button(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        about_page.click_on(about_page.CONTACT_US)
        contact_page = ContactPage(driver)
        contact_page.assert_page_is_displayed()

    @allure.title("Verify user is redirected from 'ABOUT' to 'SHOP' via 'SHOP NOW' button")
    def test_click_shop_now_button(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        about_page.click_on(about_page.SHOP_NOW)
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()
