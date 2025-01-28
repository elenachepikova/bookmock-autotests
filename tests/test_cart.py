import allure

from elements import Cart, NavigationPanel, SearchAndFilter, ProductModal
from pages import HomePage, ShopPage, ProductPage
from data import products


@allure.suite("'Cart' sidebar")
class TestCart:
    twilight = products["Twilight"]
    harry_potter = products["Harry Potter"]
    happiness = products["Happiness"]

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

    @allure.title("Add regular product to cart from HOME page")
    def test_add_product_to_cart(self, driver):


        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()

        search_sidebar = SearchAndFilter(driver)
        search_sidebar.fill_in_search_field('twilight')
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

    @allure.title("Add regular product to cart from Product page")
    def test_add_several_products_to_cart(self, driver):
        qty = 3
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.check_non_fiction_checkbox()
        shop_page.click_on_product_link()
        product_page = ProductPage(driver)
        product_page.set_quantity(qty)
        product_page.click_on_add_to_cart_button()
        cart = Cart(driver)
        cart.assert_cart_is_displayed()
        cart.assert_cart_items_count(1)
        cart.assert_product_name(self.happiness["title"])
        cart.assert_product_price(self.happiness["price"])
        cart.assert_cart_total(qty)
