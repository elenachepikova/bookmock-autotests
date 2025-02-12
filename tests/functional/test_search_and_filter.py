import allure
import pytest

from data import products
from elements import SearchAndFilter
from pages import HomePage


@pytest.mark.functional
@allure.suite("'Search and Filter' sidebar on 'Home' page")
class TestSearchAndFilterSidebar:
    harry_potter = products["Harry Potter"]["title"]
    twilight = products["Twilight"]["title"]

    @pytest.mark.smoke
    @allure.title("Open 'Search and Filter' sidebar")
    def test_open_search_and_filter_sidebar(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.assert_search_and_filter_sidebar_is_displayed()
        search_sidebar.click_on_close_icon()
        search_sidebar.assert_search_and_filter_sidebar_is_not_displayed()

    @pytest.mark.regression
    @pytest.mark.parametrize("value, title", [("har", harry_potter), ("twi", twilight)])
    @allure.title("Filter Featured section by product name Search")
    def test_search_by_name(self, driver, value, title):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.fill_in_search_field(value)
        search_sidebar.click_on_apply_button()
        homepage.assert_products_count(1)
        homepage.assert_first_book_title(title)

    @pytest.mark.regression
    @allure.title("Clear product name search on 'Search and Filter' sidebar")
    def test_clear_search_filter(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.fill_in_search_field("twi")
        search_sidebar.click_on_apply_button()
        homepage.assert_products_count(1)
        homepage.assert_first_book_title(self.twilight)
        homepage.click_on_search_and_filter_button()
        search_sidebar.click_on_clear_filter_button()
        homepage.assert_products_count(2)

    @pytest.mark.regression
    @allure.title("Filter Featured products by Popular collection")
    def test_filter_by_popular_collection(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.assert_products_count(2)
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.check_popular_checkbox()
        search_sidebar.click_on_apply_button()
        homepage.assert_products_count(1)
        homepage.assert_first_book_title(self.harry_potter)

    @pytest.mark.regression
    @allure.title("Filter Featured products by Fiction collection")
    def test_filter_by_fiction_collection(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.assert_products_count(2)
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.check_fiction_checkbox()
        search_sidebar.click_on_apply_button()
        homepage.assert_products_count(2)

    @pytest.mark.regression
    @allure.title("Filter Featured products by all collections")
    def test_filter_by_collections(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.assert_products_count(2)
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.check_popular_checkbox()
        search_sidebar.check_fiction_checkbox()
        search_sidebar.click_on_apply_button()
        homepage.assert_products_count(2)

    @pytest.mark.regression
    @allure.title("Clear Collections filter on 'Search and Filter' sidebar")
    def test_clear_collections_filter(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.check_popular_checkbox()
        search_sidebar.click_on_apply_button()
        homepage.assert_products_count(1)
        homepage.click_on_search_and_filter_button()
        search_sidebar.click_on_clear_filter_button()
        homepage.assert_products_count(2)

    @pytest.mark.regression
    @pytest.mark.parametrize(
        "price_min, price_max, title", [(18, 20, harry_potter), (20, 25, twilight)]
    )
    @allure.title("Filter Featured products by Price")
    def test_filter_by_price(self, driver, price_min, price_max, title):
        homepage = HomePage(driver)
        homepage.open()
        homepage.assert_products_count(2)
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.fill_in_price_min_field(price_min)
        search_sidebar.fill_in_price_max_field(price_max)
        search_sidebar.click_on_apply_button()
        homepage.assert_products_count(1)
        homepage.assert_first_book_title(title)

    @pytest.mark.regression
    @allure.title("No products found message if search is unsuccessful")
    def test_no_matches_found(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.fill_in_price_min_field(25)
        search_sidebar.fill_in_price_max_field(26)
        search_sidebar.click_on_apply_button()
        homepage.assert_no_results_found_message()
