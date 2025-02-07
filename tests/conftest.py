import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data import CustomerDB


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()

    # Check env variable HEADLESS
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if headless:
        options.add_argument("--headless=new")  # enable headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture(autouse=True, scope="function")
def customer_db():
    customer_db = CustomerDB()
    customer_data = customer_db.get_customer_from_db()

    yield customer_data

    customer_db.close()
