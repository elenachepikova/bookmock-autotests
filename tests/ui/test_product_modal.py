import allure
import pytest

from data import products
from elements import SearchAndFilter, ProductModal
from pages import HomePage, ShopPage


@pytest.mark.ui
@allure.suite("Product modal")
class TestProductModal:
    harry_potter = products["Harry Potter"]["title"]
    twilight = products["Twilight"]["title"]
    happiness = products["Happiness"]["title"]

    @allure.title("Open regular Product modal from 'Featured' section on HOME page")
    def test_open_regular_product_modal_from_home_page(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.fill_in_price_min_field(20)
        search_sidebar.click_on_apply_button()
        homepage.click_on_add_to_cart_button()
        homepage.switch_to_frame()
        product_modal = ProductModal(driver)
        product_modal.assert_product_elements()
        product_modal.assert_original_price_absence()
        product_modal.assert_cover_selector_absence()
        product_modal.click_on_close_icon()
        homepage.assert_products_count(1)
        homepage.assert_first_book_title(self.twilight)

    @allure.title(
        "Open Product modal for discounted product from 'All Products' section on SHOP page"
    )
    def test_open_on_sale_product_modal_from_shop_page(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_non_fiction_checkbox()
        shop_page.click_on_add_to_cart_button()
        shop_page.switch_to_frame()
        product_modal = ProductModal(driver)
        product_modal.assert_product_elements()
        product_modal.assert_original_price_presence()
        product_modal.assert_cover_selector_absence()
        product_modal.click_on_close_icon()
        shop_page.assert_products_count(1)
        shop_page.assert_first_book_title(self.happiness)

    @allure.title(
        "Open Product modal for product with cover options from 'All Products' section on SHOP page"
    )
    def test_open_with_options_product_modal_from_shop_page(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_popular_checkbox()
        shop_page.click_on_add_to_cart_button()
        shop_page.switch_to_frame()
        product_modal = ProductModal(driver)
        product_modal.assert_product_elements()
        product_modal.assert_original_price_absence()
        product_modal.assert_cover_selector_presence()
        product_modal.click_on_close_icon()
        shop_page.assert_products_count(1)
        shop_page.assert_first_book_title(self.harry_potter)
