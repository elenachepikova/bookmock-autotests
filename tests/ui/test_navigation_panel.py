import allure
import pytest

from elements import NavigationPanel, Cart
from pages import AboutPage, ContactPage, HomePage, ShopPage, FAQPage


@pytest.mark.ui
@allure.suite("Navigation panel")
class TestNavigationPanel:

    @allure.title("Open 'ABOUT' page via navigation panel")
    def test_open_about_page_via_nav_panel(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on_about_item()
        about_page = AboutPage(driver)
        about_page.assert_page_is_displayed()

    @allure.title("Open 'SHOP' page via navigation panel")
    def test_open_shop_page_via_nav_panel(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on_shop_item()
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()

    @allure.title("Open 'FAQ' page via navigation panel")
    def test_open_faq_page_via_nav_panel(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on_faq_item()
        faq_page = FAQPage(driver)
        faq_page.assert_page_is_displayed()

    @allure.title("Open 'CONTACT' page via navigation panel")
    def test_open_contact_page_via_nav_panel(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on_contact_item()
        contact_page = ContactPage(driver)
        contact_page.assert_page_is_displayed()

    @allure.title("Open 'HOME' page via navigation panel")
    def test_open_home_page_via_nav_panel(self, driver):
        contact_page = ContactPage(driver)
        contact_page.open()
        panel = NavigationPanel(driver)
        panel.click_on_home_item()
        homepage = HomePage(driver)
        homepage.assert_page_is_displayed()

    @allure.title("Click on site logo redirects to 'HOME' page")
    def test_click_on_logo_in_nav_panel(self, driver):
        faq_page = FAQPage(driver)
        faq_page.open()
        panel = NavigationPanel(driver)
        panel.click_on_logo()
        homepage = HomePage(driver)
        homepage.assert_page_is_displayed()

    @allure.title("'SHOP NOW' button redirects to 'SHOP' page")
    def test_click_on_show_now_button_in_nav_panel(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on_shop_now_button()
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()

    @allure.title("'CART' icon opens Cart sidebar")
    def test_open_empty_cart(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        header = NavigationPanel(driver)
        header.click_on_cart_icon()
        cart = Cart(driver)
        cart.assert_cart_sidebar_is_displayed()
