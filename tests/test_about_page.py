import allure

from pages import AboutPage, ContactPage, ShopPage


@allure.suite("'ABOUT' page")
class TestAboutPage:

    @allure.title("User is redirected to 'CONTACT' page  via 'CONTACT US' button")
    def test_click_contact_us_button(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        about_page.click_on_contact_us_button()
        contact_page = ContactPage(driver)
        contact_page.assert_page_is_displayed()

    @allure.title("User is redirected to 'SHOP' page via 'SHOP NOW' button")
    def test_click_shop_now_button(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        about_page.click_on_shop_now_button()
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()
