import allure
import pytest

from data import HARRY_POTTER_TITLE, TWILIGHT_TITLE
from elements import Footer, NavigationPanel, SortByDropdown
from pages import HomePage, ShopPage


@allure.suite("'HOME' page")
class TestHomePage:

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
        homepage.assert_sections_are_present()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()

    @allure.title("'SHOP' link in Featured section redirects user to SHOP page")
    def test_click_shop_link(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_shop_link()
        shop_page = ShopPage(driver)
        shop_page.assert_page_is_displayed()

    # UNSTABLE!!!
    @pytest.mark.parametrize("dropdown_option, title",
                             [(lambda dropdown: dropdown.sort_by_recently_added(), TWILIGHT_TITLE),
                              (lambda dropdown: dropdown.sort_by_price_low_high(), HARRY_POTTER_TITLE),
                              (lambda dropdown: dropdown.sort_by_price_high_low(), TWILIGHT_TITLE),
                              (lambda dropdown: dropdown.sort_by_name_a_z(), HARRY_POTTER_TITLE),
                              (lambda dropdown: dropdown.sort_by_name_z_a(), TWILIGHT_TITLE)])
    @allure.title("Sort Featured section items with 'Sort By' drop-down")
    def test_sort_featured_products(self, driver, dropdown_option, title):
        homepage = HomePage(driver)
        homepage.open()
        dropdown = SortByDropdown(driver)
        dropdown_option(dropdown)
        # time.sleep(7)
        homepage.assert_first_book_title(title)
