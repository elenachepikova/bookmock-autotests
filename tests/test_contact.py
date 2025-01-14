import allure

from elements import Footer, NavigationPanel
from pages import ContactPage, FormSubmittedPage, HomePage


@allure.suite("Tests for 'CONTACT' page")
class TestContactPage:

    @allure.title("Verify 'CONTACT' page is accessible via navigation panel")
    def test_open_contact_page(self, driver):
        homepage = HomePage(driver)
        homepage.open()
        panel = NavigationPanel(driver)
        panel.click_on(panel.CONTACT)
        contact_page = ContactPage(driver)
        contact_page.assert_page_is_displayed()

    @allure.title("Verify all expected elements are present on 'CONTACT' page")
    def test_assert_contact_page_ui(self, driver):
        contact_page = ContactPage(driver)
        contact_page.open()
        header = NavigationPanel(driver)
        header.assert_header_is_displayed()
        contact_page.assert_sections_are_present()
        footer = Footer(driver)
        footer.assert_footer_is_displayed()

    @allure.title("'Contact Us' form can be successfully submitted if all fields are filled in")
    def test_submit_contact_us_form(self, ff_driver):
        contact_page = ContactPage(ff_driver)
        contact_page.open()
        contact_page.fill_in_contact_us_form()
        form_submitted = FormSubmittedPage(ff_driver)
        form_submitted.assert_page_is_displayed()
