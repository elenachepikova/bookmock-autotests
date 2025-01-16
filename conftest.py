import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data import CustomerDB


@pytest.fixture(scope="function")
def ff_driver():
    options = FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(
        options=options, service=FirefoxService(GeckoDriverManager().install())
    )
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


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
    customer_db.create_database()

    for _ in range(10):
        first_name, last_name, email, message = customer_db.generate_random_customer()
        customer_db.insert_customer(first_name, last_name, email, message)

    customer_data = customer_db.get_customer_from_db()

    yield customer_data

    customer_db.close()
