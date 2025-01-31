import allure
import pytest

from elements import Footer, NavigationPanel
from pages import FAQPage


@pytest.mark.ui
@allure.suite("'FAQ' page")
class TestFAQPage:

    @allure.title("All expected elements are present on 'FAQ' page")
    def test_assert_faq_page_ui(self, driver):
        faq_page = FAQPage(driver)
        faq_page.open()
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        faq_page.assert_faq_page_ui()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()
