import allure
import pytest

from data import products
from elements import Footer, NavigationPanel, SortByDropdown
from pages import HomePage, ShopPage


@pytest.mark.ui
@allure.suite("'HOME' page")
class TestHomePage:
    harry_potter = products["Harry Potter"]["title"]
    twilight = products["Twilight"]["title"]

    @allure.title("'HOME' page is accessible")
    def test_open_homepage(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.assert_page_is_displayed()

    @allure.title("All expected elements are present on 'HOME' page")
    def test_assert_homepage_ui(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        homepage.assert_home_page_ui()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()

    @allure.title("'SHOP' link in Featured section redirects user to SHOP page")
    def test_click_shop_link(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_shop_link()
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()

    @pytest.mark.parametrize(
        "dropdown_option, title",
        [
            (lambda dropdown: dropdown.sort_by_recently_added(), twilight),
            (lambda dropdown: dropdown.sort_by_price_low_high(), harry_potter),
            (lambda dropdown: dropdown.sort_by_price_high_low(), twilight),
            (lambda dropdown: dropdown.sort_by_name_a_z(), harry_potter),
            (lambda dropdown: dropdown.sort_by_name_z_a(), twilight),
        ],
    )
    @allure.title("Sort Featured section items with 'Sort By' drop-down")
    def test_sort_featured_products(self, driver, dropdown_option, title):
        homepage = HomePage(driver)
        homepage.open()
        dropdown = SortByDropdown(driver)
        dropdown_option(dropdown)
        homepage.assert_first_book_title(title)
