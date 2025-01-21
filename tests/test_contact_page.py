import allure
import pytest

from elements import Footer, NavigationPanel
from pages import ContactPage, FormSubmittedPage


@allure.suite("'CONTACT' page")
class TestContactPage:

    @allure.title("All expected elements are present on 'CONTACT' page")
    def test_assert_contact_page_ui(self, driver):
        contact_page = ContactPage(driver)
        contact_page.open()
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        contact_page.assert_sections_are_present()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()

    # DRAFT VERSION, TEST NEEDS TO BE REVIEWED
    @pytest.mark.xfail
    @allure.title("'Contact Us' form can be successfully submitted if all fields are filled in")
    def test_submit_contact_us_form(self, driver, customer_db):
        contact_page = ContactPage(driver, customer_db)
        contact_page.open()
        contact_page.fill_in_contact_us_form()
        form_submitted = FormSubmittedPage(driver)
        form_submitted.assert_page_is_displayed()
