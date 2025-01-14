import allure

from elements import NavigationPanel
from pages import HomePage, ShopPage


@allure.suite("'SHOP' page")
class TestShopPage:

    @allure.title("'SHOP' page is accessible via navigation panel")
    def test_open_shop_page(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on_shop_item()
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()
