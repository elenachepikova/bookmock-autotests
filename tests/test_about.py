import allure

from elements import NavigationPanel
from pages import AboutPage, ContactPage, HomePage, ShopPage


@allure.suite("'ABOUT' page")
class TestAboutPage:

    @allure.title("'ABOUT' page is accessible via navigation panel")
    def test_open_about_page(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on_about_item()
        about_page = AboutPage(driver)
        about_page.assert_page_is_displayed()

    @allure.title("User is redirected from 'ABOUT' to 'CONTACT' via 'CONTACT US' button")
    def test_click_contact_us_button(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        about_page.click_on_contact_us_button()
        contact_page = ContactPage(driver)
        contact_page.assert_page_is_displayed()

    @allure.title("User is redirected from 'ABOUT' to 'SHOP' via 'SHOP NOW' button")
    def test_click_shop_now_button(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        about_page.click_on_shop_now_button()
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()
