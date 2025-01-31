import allure
import pytest

from elements import NavigationPanel, Footer, SortByDropdown
from pages import ShopPage
from data import products


@allure.suite("'SHOP' page")
class TestShopPage:
    harry_potter = products["Harry Potter"]["title"]
    twilight = products["Twilight"]["title"]
    happiness = products["Happiness"]["title"]

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

    @pytest.mark.parametrize(
        "value, title", [("har", harry_potter), ("twi", twilight), ("sci", happiness)]
    )
    @allure.title("Filter Featured section by product name Search")
    def test_search_by_name(self, driver, value, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.apply_search_filter(value)
        shop_page.assert_products_count(1)
        shop_page.assert_first_book_title(title)

    @allure.title("Clear search by product name on 'SHOP' page")
    def test_clear_search_filter(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.apply_search_filter("gre")
        shop_page.assert_products_count(1)
        shop_page.assert_first_book_title(self.happiness)
        shop_page.clear_search_filter()
        shop_page.assert_products_count(3)

    @pytest.mark.parametrize(
        "check_checkbox, value, title",
        [
            (lambda shop_page: shop_page.check_featured_checkbox(), 2, twilight),
            (lambda shop_page: shop_page.check_on_sale_checkbox(), 1, happiness),
            (lambda shop_page: shop_page.check_in_stock_checkbox(), 3, twilight),
        ],
    )
    @allure.title("Filter ALL products by 'Browse By' filter")
    def test_filter_by_browse_by(self, driver, check_checkbox, value, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.assert_products_count(3)
        check_checkbox(shop_page)
        shop_page.assert_products_count(value)
        shop_page.assert_first_book_title(title)

    @pytest.mark.parametrize(
        "check_checkbox, value, title",
        [
            (lambda shop_page: shop_page.check_fiction_checkbox(), 2, twilight),
            (lambda shop_page: shop_page.check_non_fiction_checkbox(), 1, happiness),
            (lambda shop_page: shop_page.check_popular_checkbox(), 1, harry_potter),
        ],
    )
    @allure.title("Filter ALL products by 'Collections' filter")
    def test_filter_by_collections(self, driver, check_checkbox, value, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.assert_products_count(3)
        check_checkbox(shop_page)
        shop_page.assert_products_count(value)
        shop_page.assert_first_book_title(title)

    @pytest.mark.parametrize(
        "price_min, price_max, title",
        [(8, 10, happiness), (10, 20, harry_potter), (20, 100, twilight)],
    )
    @allure.title("Filter ALL products by Price")
    def test_filter_by_price(self, driver, price_min, price_max, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.assert_products_count(3)
        shop_page.fill_in_price_min_field(price_min)
        shop_page.fill_in_price_max_field(price_max)
        shop_page.assert_products_count(1)
        shop_page.assert_first_book_title(title)

    @allure.title("No products found message if search is unsuccessful")
    def test_no_matches_found(self, driver):
        shop_page = ShopPage(driver)
        shop_page.open()
        shop_page.fill_in_price_min_field(10)
        shop_page.fill_in_price_max_field(20)
        shop_page.check_non_fiction_checkbox()
        shop_page.assert_no_results_found_message()

    @pytest.mark.parametrize(
        "dropdown_option, title",
        [
            (lambda dropdown: dropdown.sort_by_recently_added(), twilight),
            (lambda dropdown: dropdown.sort_by_price_low_high(), happiness),
            (lambda dropdown: dropdown.sort_by_price_high_low(), twilight),
            (lambda dropdown: dropdown.sort_by_name_a_z(), harry_potter),
            (lambda dropdown: dropdown.sort_by_name_z_a(), twilight),
        ],
    )
    @allure.title("Sort Featured section items with 'Sort By' drop-down")
    def test_sort_all_products(self, driver, dropdown_option, title):
        shop_page = ShopPage(driver)
        shop_page.open()
        dropdown = SortByDropdown(driver)
        dropdown_option(dropdown)
        shop_page.assert_first_book_title(title)
