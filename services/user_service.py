import allure

from core import BaseService, assert_response_code


class UserService(BaseService):

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
        assert_response_code(response)

        user_data = response.json()
        assertion(user_data, body_req)

    @allure.step("Update user by username and assert response code and body")
    def update_user_and_assert(self, username, body_req, assertion):
        response = self.update_user(body_req, username)
        assert_response_code(response)

        user_data = response.json()
        assertion(user_data)
