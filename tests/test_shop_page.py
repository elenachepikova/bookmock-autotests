import allure
import pytest

from elements import NavigationPanel, Footer, SortByDropdown
from pages import ShopPage
from data import HARRY_POTTER_TITLE, TWILIGHT_TITLE, HAPPINESS_TITLE


@allure.suite("'SHOP' page")
class TestShopPage:

    @allure.title("Assert all expected elements are present on 'SHOP' page")
    def test_assert_shop_page_ui(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        shop_page.assert_all_products_section_ui()
        shop_page.assert_products_count(3)
        footer = Footer(driver)
        footer.assert_footer_is_displayed()

    @pytest.mark.parametrize("value, title",
                             [("har", HARRY_POTTER_TITLE),
                              ("twi", TWILIGHT_TITLE),
                              ("sci", HAPPINESS_TITLE)])
    @allure.title("Filter Featured section by product name Search")
    def test_search_by_name(self, driver, value, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.fill_in_search_field(value)
        shop_page.click_on_search_button()
        shop_page.assert_products_count(1)
        shop_page.assert_first_book_title(title)

    @allure.title("Clear search by product name on 'SHOP' page")
    def test_clear_search_filter(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.fill_in_search_field("gre")
        shop_page.click_on_search_button()
        shop_page.assert_products_count(1)
        shop_page.assert_first_book_title(HAPPINESS_TITLE)
        shop_page.clear_search_filter()
        shop_page.assert_products_count(3)

    @pytest.mark.parametrize("check_checkbox, value, title",
                             [(lambda shop_page: shop_page.check_featured_checkbox(), 2, TWILIGHT_TITLE),
                              (lambda shop_page: shop_page.check_on_sale_checkbox(), 1, HAPPINESS_TITLE),
                              (lambda shop_page: shop_page.check_in_stock_checkbox(), 3, TWILIGHT_TITLE)])
    @allure.title("Filter ALL products by 'Browse By' filter")
    def test_filter_by_browse_by(self, driver, check_checkbox, value, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.assert_products_count(3)
        check_checkbox(shop_page)
        shop_page.assert_products_count(value)
        shop_page.assert_first_book_title(title)

    @pytest.mark.parametrize("check_checkbox, value, title",
                             [(lambda shop_page: shop_page.check_fiction_checkbox(), 2, TWILIGHT_TITLE),
                              (lambda shop_page: shop_page.check_non_fiction_checkbox(), 1, HAPPINESS_TITLE),
                              (lambda shop_page: shop_page.check_popular_checkbox(), 1, HARRY_POTTER_TITLE)])
    @allure.title("Filter ALL products by 'Collections' filter")
    def test_filter_by_collections(self, driver, check_checkbox, value, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.assert_products_count(3)
        check_checkbox(shop_page)
        shop_page.assert_products_count(value)
        shop_page.assert_first_book_title(title)

    @pytest.mark.parametrize("price_min, price_max, title",
                             [(8, 10, HAPPINESS_TITLE),
                              (10, 20, HARRY_POTTER_TITLE),
                              (20, 100, TWILIGHT_TITLE)])
    @allure.title("Filter ALL products by Price")
    def test_filter_by_price(self, driver, price_min, price_max, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.assert_products_count(3)
        shop_page.fill_in_price_min_field(price_min)
        shop_page.fill_in_price_max_field(price_max)
        shop_page.assert_products_count(1)
        shop_page.assert_first_book_title(title)

    @allure.title("No products found message is displayed on 'SHOP' page if search is unsuccessful")
    def test_no_matches_found(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.fill_in_price_min_field(10)
        shop_page.fill_in_price_max_field(20)
        shop_page.check_non_fiction_checkbox()
        shop_page.assert_no_results_found_message()

    @pytest.mark.parametrize("dropdown_option, title",
                             [(lambda dropdown: dropdown.sort_by_recently_added(), TWILIGHT_TITLE),
                              (lambda dropdown: dropdown.sort_by_price_low_high(), HAPPINESS_TITLE),
                              (lambda dropdown: dropdown.sort_by_price_high_low(), TWILIGHT_TITLE),
                              (lambda dropdown: dropdown.sort_by_name_a_z(), HARRY_POTTER_TITLE),
                              (lambda dropdown: dropdown.sort_by_name_z_a(), TWILIGHT_TITLE)])
    @allure.title("Sort Featured section items with 'Sort By' drop-down")
    def test_sort_all_products(self, driver, dropdown_option, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        dropdown = SortByDropdown(driver)
        dropdown_option(dropdown)
        shop_page.assert_first_book_title(title)
