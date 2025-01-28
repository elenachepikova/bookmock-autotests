import allure

from data import HARRY_POTTER_TITLE, HAPPINESS_TITLE
from elements import Footer, NavigationPanel, SearchAndFilter
from pages import HomePage, ShopPage, ProductPage


@allure.suite("Product page")
class TestProductPage:
    path_twi = "untitled-product-1"
    path_hp = "untitled-product-2"
    path_sci = "untitled-product-3"

    @allure.title("Open Product page from 'Featured' section on HOME page")
    def test_open_product_page_from_home(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.fill_in_search_field("harry")
        search_sidebar.click_on_apply_button()
        homepage.click_on_product_link()
        product_page = ProductPage(driver)
        product_page.assert_page_is_displayed(HARRY_POTTER_TITLE, self.path_hp)

    @allure.title("Open Product page from 'All Products' section on SHOP page")
    def test_open_product_page_from_shop(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_on_sale_checkbox()
        shop_page.click_on_product_link()
        product_page = ProductPage(driver)
        product_page.assert_page_is_displayed(HAPPINESS_TITLE, self.path_sci)
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()

    @allure.title("Assert page UI for regular Product")
    def test_regular_product_page(self, driver):
        product_page = ProductPage(driver)
        product_page.open(self.path_twi)
        product_page.assert_product_page_ui()
        product_page.assert_original_price_absence()
        product_page.assert_cover_selector_absence()

    @allure.title("Assert page UI for Product on sale")
    def test_product_on_sale_page(self, driver):
        product_page = ProductPage(driver)
        product_page.open(self.path_sci)
        product_page.assert_product_page_ui()
        product_page.assert_original_price_presence()
        product_page.assert_cover_selector_absence()

    @allure.title("Assert page UI for Product with Cover options")
    def test_product_with_cover_options_page(self, driver):
        product_page = ProductPage(driver)
        product_page.open(self.path_hp)
        product_page.assert_product_page_ui()
        product_page.assert_original_price_absence()
        product_page.assert_cover_selector_presence()
