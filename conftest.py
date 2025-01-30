import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data import CustomerDB


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture(autouse=True, scope="session")
def customer_db():
    customer_db = CustomerDB()
    customer_data = customer_db.get_customer_from_db()

    yield customer_data

    customer_db.close()
