import allure

from core import APIAssertions


class UserService(APIAssertions):

    def __init__(self, headers):
        super().__init__()
        self.BASE_URL = "https://petstore.swagger.io/v2/user"
        self.headers = headers

    @staticmethod
    def _check_response(response):
        if response.headers.get("Content-Type") != "application/json":
            raise ValueError(
                f'Invalid Content-Type: {response.headers.get("Content-Type")}'
            )
        return response

    @allure.step("Get user by username")
    def get_user(self, username):
        response = self.get(f"{self.BASE_URL}/{username}", headers=self.headers)
        self._check_response(response)
        return response

    @allure.step("Create users with list provided")
    def create_with_list(self, user_list):
        response = self.post(
            f"{self.BASE_URL}/createWithList", headers=self.headers, json=user_list
        )
        self._check_response(response)
        return response

    @allure.step("Delete user by username")
    def delete_user(self, username):
        response = self.delete(f"{self.BASE_URL}/{username}", headers=self.headers)
        self._check_response(response)
        return response

    @allure.step("Update user by username")
    def update_user(self, user_data, username):
        response = self.put(
            f"{self.BASE_URL}/{username}", headers=self.headers, json=user_data
        )
        self._check_response(response)
        return response

    @allure.step("Get user by username and assert response code and body")
    def get_user_and_assert(self, username, body_req, assertion):
        response = self.get_user(username)
        self.assert_response_code(response)

        user_data = response.json()
        assertion(user_data, body_req)

    @allure.step("Update user by username and assert response code and body")
    def update_user_and_assert(self, username, body_req, assertion):
        response = self.update_user(body_req, username)
        self.assert_response_code(response)

        user_data = response.json()
        assertion(user_data)

    @allure.step("Assert response for 'Create list of users with given array' endpoint")
    def assert_user_list_created_response(self, user_data):
        assert (
            user_data["code"] == 200
        ), f"Expected 'code' == 200, Actual - {user_data["code"]}"
        assert (
            user_data["type"] == "unknown"
        ), f"Expected 'type' == 'unknown', Actual - {user_data["type"]}"
        assert (
            user_data["message"] == "ok"
        ), f"Expected 'message' == 'ok', Actual - {user_data["message"]}"

    @allure.step("Assert response for 'Update user' endpoint")
    def assert_user_updated_response(self, user_data, body_req):
        assert (
            user_data["code"] == 200
        ), f"Expected 'code' == 200, Actual - {user_data["code"]}"
        assert (
            user_data["type"] == "unknown"
        ), f"Expected 'type' == 'unknown', Actual - {user_data["type"]}"
        assert user_data["message"] == str(
            body_req["id"]
        ), "Unexpected 'message' value, 'message' should be equal to user id"
