import allure

from elements import SearchAndFilter
from pages import HomePage


@allure.suite("'Search and Filter' sidebar for Featured section on 'Home' page")
class TestSearchAndFilterSidebar:

    @allure.title("'Search and Filter' sidebar is opened by click on 'Search and Filter' button")
    def test_open_search_and_filter_sidebar(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.assert_search_and_filter_sidebar_is_displayed()
        search_sidebar.click_on_close_icon()
        search_sidebar.assert_search_and_filter_sidebar_is_not_displayed()

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

    @allure.title("Filter Featured products by Fiction and Popular collections")
    def test_filter_by_fiction_collection(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.assert_products_count(2)
        homepage.click_on_search_and_filter_button()
        search_sidebar = SearchAndFilter(driver)
        search_sidebar.check_popular_checkbox()
        search_sidebar.check_fiction_checkbox()
        search_sidebar.click_on_apply_button()
        homepage.assert_products_count(2)

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
