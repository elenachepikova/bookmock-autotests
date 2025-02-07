import allure
import pytest

from core import load_json_config


@pytest.mark.api
@pytest.mark.regression
@allure.suite("Tests for user service")
@allure.sub_suite("PUT")
class TestUpdateUser:
    body_config = load_json_config("data/api/request_bodies.json")
    new_user_body = body_config["add_single_user"]
    updated_user_body = body_config["update_single_user"]

    @allure.title("Existing user can be updated using PUT /user/{username} endpoint")
    def test_update_existing_user(self, create_user, user_service):
        """
        Tests existing user data update:
        - creates new user
        - asserts new user data
        - updates created user data
        - asserts response code and body
        - asserts user data updates
        - user is preserved and will be cleaned up in the following scenarios
        """
        username = self.new_user_body[0]["username"]

        user_service.get_user_and_assert(
            username, self.new_user_body, user_service.assert_response_full
        )
        user_service.update_user_and_assert(
            username,
            self.updated_user_body,
            lambda response: user_service.assert_user_updated_response(
                response, self.updated_user_body
            ),
        )
        user_service.get_user_and_assert(
            username, self.updated_user_body, user_service.assert_response_full
        )

    @allure.title(
        "Error 404 is displayed on attempt to update not existing user with invalid username"
    )
    @pytest.mark.xfail(reason="existing bug: 200 OK instead of 404 err in response")
    @pytest.mark.parametrize("username", ["invalid_usr333", " "])
    def test_error_on_update_invalid_username(self, user_service, username):
        """
        Tests that attempt to update user by invalid username (not existing or empty) results in 404 error
        """
        response = user_service.update_user(self.updated_user_body, username)
        user_service.assert_response_code(response, 404)

    @allure.title(
        "Error 400 is displayed on attempt to update existing user with invalid user data (empty body)"
    )
    @pytest.mark.xfail(reason="existing bug: 200 OK instead of 400 err in response")
    def test_error_on_update_invalid_body(self, cleanup_user, user_service):
        """
        Tests that attempt to update user with empty request body results in 400 error
        - user created in test_update_existing_user is cleaned up
        """
        username = self.new_user_body[0]["username"]
        body = {}
        cleanup_user.append(username)

        response = user_service.update_user(body, username)
        user_service.assert_response_code(response, 400)
