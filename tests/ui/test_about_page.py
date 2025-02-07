import allure
import pytest

from pages import AboutPage, ContactPage, ShopPage
from elements import NavigationPanel, Footer


@pytest.mark.ui
@allure.suite("'ABOUT' page")
class TestAboutPage:

    @pytest.mark.smoke
    @allure.title("All expected elements are present on 'ABOUT' page")
    def test_assert_about_ui(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        about_page.assert_about_page_ui()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()

    @pytest.mark.regression
    @allure.title("User is redirected to 'CONTACT' page  via 'CONTACT US' button")
    def test_click_contact_us_button(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        about_page.click_on_contact_us_button()
        contact_page = ContactPage(driver)
        contact_page.assert_page_is_displayed()

    @pytest.mark.regression
    @allure.title("User is redirected to 'SHOP' page via 'SHOP NOW' button")
    def test_click_shop_now_button(self, driver):
        about_page = AboutPage(driver)
        about_page.open()
        about_page.click_on_shop_now_button()
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()
