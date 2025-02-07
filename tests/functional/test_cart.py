import allure
import pytest

from data import products
from elements import Cart, NavigationPanel, SearchAndFilter, ProductModal
from pages import HomePage, ShopPage, ProductPage


@pytest.mark.functional
@allure.suite("'Cart' sidebar")
class TestCart:
    twilight = products["Twilight"]
    harry_potter = products["Harry Potter"]
    happiness = products["Happiness"]

    @pytest.mark.smoke
    @allure.title("CART sidebar can be opened via 'HOME' page")
    def test_open_empty_cart(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        header = NavigationPanel(driver)
        header.click_on_cart_icon()
        cart = Cart(driver)
        cart.assert_empty_cart_is_displayed()
        cart.click_on_close_icon()
        cart.assert_cart_is_not_displayed()

    @pytest.mark.smoke
    @allure.title("Add regular product to cart from HOME page")
    def test_add_product_to_cart(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.fill_in_search_field("twilight")
        search_sidebar.click_on_apply_button()
        homepage.click_on_add_to_cart_button()
        homepage.switch_to_frame()
        product_modal = ProductModal(driver)
        product_modal.click_on_add_to_cart_button()
        product_modal.switch_to_default_content()
        cart = Cart(driver)
        cart.assert_cart_is_displayed()
        cart.assert_cart_items_count(1)
        cart.assert_product_name(self.twilight["title"])
        cart.assert_product_price(self.twilight["price"])
        cart.assert_cart_total()

    @pytest.mark.regression
    @allure.title("Add product with cover options to cart from SHOP page")
    def test_add_product_with_options_to_cart(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_popular_checkbox()
        shop_page.click_on_add_to_cart_button()
        shop_page.switch_to_frame()
        product_modal = ProductModal(driver)
        product_modal.select_hard_cover()
        product_modal.click_on_add_to_cart_button()
        product_modal.switch_to_default_content()
        cart = Cart(driver)
        cart.assert_cart_is_displayed()
        cart.assert_cart_items_count(1)
        cart.assert_product_name(self.harry_potter["title"])
        cart.assert_product_price(self.harry_potter["price"])
        cart.assert_cart_total()

    @pytest.mark.regression
    @allure.title("Add regular product to cart from Product page")
    def test_add_several_products_to_cart(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_non_fiction_checkbox()
        shop_page.click_on_product_link()
        product_page = ProductPage(driver)
        product_page.set_quantity(3)
        product_page.click_on_add_to_cart_button()
        cart = Cart(driver)
        cart.assert_cart_is_displayed()
        cart.assert_cart_items_count(1)
        cart.assert_product_name(self.happiness["title"])
        cart.assert_product_price(self.happiness["price"])
        cart.assert_cart_total()

    @pytest.mark.smoke
    @allure.title("Remove added product from cart")
    def test_remove_product_from_cart(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_on_sale_checkbox()
        shop_page.click_on_product_link()
        product_page = ProductPage(driver)
        product_page.click_on_add_to_cart_button()
        cart = Cart(driver)
        cart.assert_cart_is_displayed()
        cart.set_quantity("0")
        cart.assert_empty_cart_is_displayed()

    @pytest.mark.regression
    @allure.title("Update product quantity in cart")
    def test_update_product_quantity_in_cart(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_popular_checkbox()
        shop_page.click_on_product_link()
        product_page = ProductPage(driver)
        product_page.select_soft_cover()
        product_page.click_on_add_to_cart_button()
        cart = Cart(driver)
        cart.assert_cart_is_displayed()
        cart.set_quantity("2")
        driver.refresh()
        header = NavigationPanel(driver)
        header.click_on_cart_icon()
        cart.assert_cart_total()

    @pytest.mark.regression
    @allure.title("Click on 'Continue Shopping' button in Cart")
    def test_click_continue_shopping_button(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_non_fiction_checkbox()
        shop_page.click_on_add_to_cart_button()
        shop_page.switch_to_frame()
        product_modal = ProductModal(driver)
        product_modal.click_on_add_to_cart_button()
        product_modal.switch_to_default_content()
        cart = Cart(driver)
        cart.assert_cart_is_displayed()
        cart.click_on_continue_shopping_button()
        cart.assert_cart_is_not_displayed()
        shop_page.assert_page_is_displayed()

    @pytest.mark.regression
    @allure.title("Add different products to cart")
    def test_add_different_products_to_cart(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_non_fiction_checkbox()
        shop_page.click_on_add_to_cart_button()
        shop_page.switch_to_frame()
        product_modal = ProductModal(driver)
        product_modal.click_on_add_to_cart_button()
        product_modal.switch_to_default_content()
        cart = Cart(driver)
        cart.click_on_continue_shopping_button()
        shop_page.check_non_fiction_checkbox()
        shop_page.apply_search_filter("twilight")
        shop_page.click_on_add_to_cart_button()
        shop_page.switch_to_frame()
        product_modal.click_on_add_to_cart_button()
        product_modal.switch_to_default_content()
        cart.assert_cart_items_count(2)
        cart.assert_cart_total()
