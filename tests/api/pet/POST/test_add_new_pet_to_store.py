from typing import Dict

import allure
import pytest

from core import load_json_config


@pytest.mark.api
@allure.suite("Tests for pet service")
@allure.sub_suite("POST")
class TestAddPetPost:
    body_config = load_json_config("data/api/request_bodies.json")
    req = body_config["add_pet_with_required_parameters"]
    available = body_config["add_available_pet_with_all_parameters"]
    pending = body_config["add_pending_pet_with_all_parameters"]
    sold = body_config["add_sold_pet_with_all_parameters"]

    @pytest.mark.smoke
    @allure.title("New pet can be successfully added using POST /pet endpoint")
    @pytest.mark.parametrize(
        "body_req, assertion",
        [(req, "assert_response_min"), (available, "assert_response_full")],
    )
    def test_add_pet_with_different_params_set(
        self, cleanup_pet, pet_service, body_req: Dict[str, str], assertion
    ):
        """
        Tests new pet creation:
        - create new pet with required parameters only
        - create new pet with full list of parameters
        - assert can be successfully added, assert response body and code
        - get new pet by id and assert response body is as expected
        - clean up pets
        """
        pet_id = body_req["id"]
        cleanup_pet.append(pet_id)

        assertion = getattr(pet_service, assertion)
        pet_service.add_pet_and_assert(body_req, assertion)
        pet_service.get_pet_and_assert(pet_id, body_req, assertion)

    @pytest.mark.regression
    @allure.title(
        "New pet with different parameters can be successfully added using POST /pet endpoint"
    )
    @pytest.mark.parametrize(
        "body_req, status",
        [(available, "available"), (pending, "pending"), (sold, "sold")],
    )
    def test_add_pet_with_different_statuses(
        self, cleanup_pet, pet_service, body_req, status
    ):
        """
        Tests:
        - new pet creation with different statuses (available, pending, sold)
        - assert response code, body, and pet status
        - clean up pet
        """
        pet_id = body_req["id"]
        cleanup_pet.append(pet_id)

        pet_service.add_pet_and_assert(body_req, pet_service.assert_response_full)

        response = pet_service.get_pet_by_id(pet_id)
        pet_service.assert_response_code(response)

        pet_data = response.json()
        assert pet_data["status"] == status

    @pytest.mark.regression
    @allure.title("New pet cannot be added if body does not correspond to schema")
    @pytest.mark.xfail(reason="existing bug: 500 err instead of 405 in response")
    def test_add_pet_with_invalid_params(self, pet_service):
        """
        Tests negative scenario:
        - attempts to add new pet with invalid body
        - asserts response code is 405
        - asserts new pet is not added
        """
        body_req = self.body_config["add_pet_with_invalid_parameters"]
        pet_id = body_req["id"]

        response = pet_service.add_pet(body_req)
        pet_service.assert_response_code(response, 405)

        response = pet_service.get_pet_by_id(pet_id)
        pet_service.assert_response_code(response, 404)
