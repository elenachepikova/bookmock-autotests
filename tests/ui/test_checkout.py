import allure

from elements import Cart, NavigationPanel
from pages import HomePage, ShopPage, ProductPage, CheckoutPage


@allure.suite("Checkout steps")
class TestCheckout:

    @allure.title("Go through checkout process")
    def test_place_order(self, driver, customer_db):
        homepage = HomePage(driver)
        homepage.open()
        header = NavigationPanel(driver)
        header.click_on_shop_now_button()
        shop_page = ShopPage(driver)
        shop_page.click_on_product_link()
        product_page = ProductPage(driver)
        product_page.click_on_add_to_cart_button()
        cart = Cart(driver)
        cart.click_on_checkout_button()
        checkout = CheckoutPage(driver, customer_db)
        checkout.assert_customer_info_step_opened()
        checkout.fill_in_checkout_form()
        checkout.assert_shipping_details_step_opened()
        checkout.click_on_continue_button()
        checkout.assert_payment_details_step_opened()
        checkout.click_on_submit_button()
        checkout.assert_thank_you_step_opened()
