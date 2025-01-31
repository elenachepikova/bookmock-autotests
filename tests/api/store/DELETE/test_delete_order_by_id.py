import allure
import pytest

from core import assert_response_code


@pytest.mark.api
@allure.suite("Tests for store service")
@allure.sub_suite("DELETE")
class TestOrderDelete:
    @allure.title(
        "Existing order can be successfully deleted using DELETE /store/order/{order_id} endpoint"
    )
    def test_place_and_delete_order(self, place_order, store_service):
        """
        Tests order successful deletion:
        - place new order
        - delete placed order
        - assert response code and body
        - assert order is not accessible after deletion
        """
        order_id = place_order["id"]

        response = store_service.delete_order(order_id)
        assert_response_code(response, 200)

        order_data = response.json()

        assert order_data["code"] == 200, 'Unexpected "code" key value'
        assert order_data["type"] == "unknown", 'Unexpected "type" key value'
        assert order_data["message"] == f"{order_id}", 'Unexpected "message" key value'

        response = store_service.get_order_by_id(order_id)
        assert_response_code(response, 404)

    @allure.title(
        "Error 404 is displayed on attempt to delete order by invalid order id"
    )
    @pytest.mark.parametrize(
        "order_id, message, key_type, code",
        [
            (7777, "Order Not Found", "unknown", 404),
            (
                "a",
                'java.lang.NumberFormatException: For input string: "a"',
                "unknown",
                404,
            ),
            (
                "!@#$",
                'java.lang.NumberFormatException: For input string: "!@"',
                "unknown",
                404,
            ),
        ],
    )
    def test_delete_by_invalid_order_id(
        self, store_service, order_id, message, key_type, code
    ):
        """
        Tests that attempt to delete order by invalid order_id
        (not existing, invalid type, special characters) results in 404 error
        """
        response = store_service.delete_order(order_id)
        assert_response_code(response, code)

        order_data = response.json()

        assert order_data["code"] == code, 'Unexpected "code" key value'
        assert order_data["type"] == key_type, 'Unexpected "type" key value'
        assert order_data["message"] == message, 'Unexpected "message" key value'

    @allure.title(
        "Error 405 is displayed on attempt to delete order using empty order id"
    )
    def test_delete_by_empty_order_id(self, store_service):
        """
        Tests that deletion order by empty order_id results in 405 error
        """
        response = store_service.delete_order("")

        assert_response_code(response, 405)
