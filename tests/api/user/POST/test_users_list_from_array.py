import allure
import pytest

from core import load_json_config


@pytest.mark.api
@allure.suite("Tests for user service")
@allure.sub_suite("POST")
class TestCreateUsersFromList:
    body_config = load_json_config("data/api/request_bodies.json")
    single_user = body_config["add_single_user"]
    multiple_users = body_config["add_list_of_users"]
    duplicates = body_config["duplicated_usernames"]
    empty_list = body_config["empty_list"]
    incorrect_body = body_config["incorrect_body"]

    @pytest.mark.regression
    @allure.title(
        "New user can be successfully created using POST /user/createWithList endpoint"
    )
    def test_add_single_user_via_list(self, cleanup_user, user_service):
        """
        Tests new single user creation via /user/createWithList endpoint:
        - create new user
        - assert response code and body
        - assert new user data via username
        - clean up user
        """
        response = user_service.create_with_list(self.single_user)
        response_data = response.json()
        user_service.assert_user_list_created_response(response_data)

        username = self.single_user[0]["username"]
        cleanup_user.append(username)

        user_service.get_user_and_assert(
            username, self.single_user, user_service.assert_response_full
        )

    @pytest.mark.smoke
    @allure.title(
        "New users can be successfully created using POST /user/createWithList endpoint"
    )
    def test_add_multiple_users_via_list(self, cleanup_user, user_service):
        """
        Tests multiple users creation via /user/createWithList endpoint:
        - create new users
        - assert response code and body
        - assert each of created users data via usernames
        - clean up created users
        """
        response = user_service.create_with_list(self.multiple_users)
        response_data = response.json()
        user_service.assert_user_list_created_response(response_data)

        for user in self.multiple_users:
            username = user["username"]
            cleanup_user.append(username)

            user_service.get_user_and_assert(
                username, user, user_service.assert_response_full
            )

    @pytest.mark.regression
    @allure.title("New users cannot be created if request body contains duplicates")
    @pytest.mark.xfail(reason="existing bug: 200 OK instead of 400 err in response")
    def test_error_add_duplicates(self, cleanup_user, user_service):
        """
        Tests that attempt to create several users with the same username results in 400 error
        """
        response = user_service.create_with_list(self.duplicates)
        user_service.assert_response_code(response, 400)

    @pytest.mark.regression
    @allure.title("New users cannot be created if request body is empty")
    @pytest.mark.xfail(reason="existing bug: 200 OK instead of 400 err in response")
    def test_error_add_empty_list(self, cleanup_user, user_service):
        """
        Tests that attempt to create multiple users with empty list in request body results in 400 error
        """
        response = user_service.create_with_list(self.empty_list)
        user_service.assert_response_code(response, 400)

    @pytest.mark.regression
    @allure.title("New users cannot be created if request body is invalid")
    @pytest.mark.xfail(reason="existing bug: 200 OK instead of 400 err in response")
    def test_error_add_incorrect_body(self, cleanup_user, user_service):
        """
        Tests that attempt to create multiple users with invalid list in request body results in 400 error
        """
        response = user_service.create_with_list(self.incorrect_body)
        user_service.assert_response_code(response, 400)
