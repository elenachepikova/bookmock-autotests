import allure
import pytest

from elements import Footer, NavigationPanel
from pages import ContactPage


@pytest.mark.ui
@allure.suite("'CONTACT' page")
class TestContactPage:

    @pytest.mark.smoke
    @allure.title("All expected elements are present on 'CONTACT' page")
    def test_assert_contact_page_ui(self, driver):
        contact_page = ContactPage(driver)
        contact_page.open()
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        contact_page.assert_contact_page_ui()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()
