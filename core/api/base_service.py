import logging

import allure
import requests


def create_logger():
    """Creates and configures a logger for logging requests and responses."""
    logger = logging.getLogger("BaseServiceLogger")
    logger.setLevel(logging.DEBUG)

    # Handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Handler for logging to a file
    file_handler = logging.FileHandler('base_service.log')
    file_handler.setLevel(logging.INFO)

    # Formatting log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Adding handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


class BaseService:
    def __init__(self):
        self.logger = create_logger()

    def _request(self, method, url, headers=None, body=None, code=200, json=None):
        headers = headers or {}

        try:
            # If json is present
            if json is not None:
                response = requests.request(method, url, headers=headers, json=json)
            else:
                # If json is not present
                response = requests.request(method, url, headers=headers, data=body)

            if response.status_code != code:
                self.logger.error(f"Unexpected status code: {response.status_code}. Expected {code}")
            else:
                self.logger.info(f"Request successful: {url}, Status: {response.status_code}")

        except requests.RequestException as e:
            self.logger.error(f"Request failed: {e}")
            return None

        return response

    @allure.step('GET: {url}')
    def get(self, url, headers=None, code=200):
        """Performs a GET request with logging and response validation."""
        self.logger.info("Performing GET request. URL: %s", url)
        return self._request("GET", url, headers=headers, code=code)

    @allure.step('POST: {url}')
    def post(self, url, body=None, headers=None, code=200, json=None):
        """Performs a POST request with logging and response validation."""
        self.logger.info("Performing POST request. URL: %s, Body: %s", url, body)
        return self._request("POST", url, headers=headers, body=body, code=code, json=json)

    @allure.step('PUT: {url}')
    def put(self, url, body=None, headers=None, code=200, json=None):
        """Performs a PUT request with logging and response validation."""
        self.logger.info("Performing PUT request. URL: %s, Body: %s", url, body)
        return self._request("PUT", url, headers=headers, body=body, code=code, json=json)

    @allure.step('DELETE: {url}')
    def delete(self, url, headers=None, code=200):
        """Performs a DELETE request with logging and response validation."""
        self.logger.info("Performing DELETE request. URL: %s", url)
        return self._request("DELETE", url, headers=headers, code=code)
