import allure

from core import APIAssertions


class StoreService(APIAssertions):

    def __init__(self, headers):
        super().__init__()
        self.BASE_URL = "https://petstore.swagger.io/v2/store/order"
        self.headers = headers

    @staticmethod
    def _check_response(response):
        if response.headers.get("Content-Type") != "application/json":
            raise ValueError(
                f'Invalid Content-Type: {response.headers.get("Content-Type")}'
            )
        return response

    @allure.step("Get order by ID")
    def get_order_by_id(self, order_id):
        response = self.get(f"{self.BASE_URL}/{order_id}", headers=self.headers)
        self._check_response(response)
        return response

    @allure.step("Place new order")
    def place_order(self, order_data):
        response = self.post(f"{self.BASE_URL}", headers=self.headers, json=order_data)
        self._check_response(response)
        return response

    @allure.step("Delete order by ID")
    def delete_order(self, order_id):
        response = self.delete(f"{self.BASE_URL}/{order_id}", headers=self.headers)
        self._check_response(response)
        return response
