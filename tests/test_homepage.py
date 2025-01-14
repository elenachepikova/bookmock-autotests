import allure

from elements import Footer, NavigationPanel
from pages import HomePage


@allure.suite("Tests for 'HOME' page")
class TestHomePage:

    @allure.title("Verify 'HOME' page is accessible")
    def test_open_homepage(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        homepage.assert_page_is_displayed()

    @allure.title("Verify all expected elements are present on 'HOME' page")
    def test_assert_homepage_ui(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        homepage.assert_sections_are_present()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()
