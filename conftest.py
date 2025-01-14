import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


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

