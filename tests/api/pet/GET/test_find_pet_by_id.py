import allure
import pytest

from core import assert_response_full, assert_response_code


@pytest.mark.api
@allure.suite("Tests for pet service")
@allure.sub_suite("GET")
class TestPetGet:
    @allure.title(
        "Existing pet data can be successfully retrieved using GET /pet/{pet_id} endpoint"
    )
    def test_find_pet_by_valid_id(self, create_pet, cleanup_pet, pet_service):
        """
        Tests retrieving pet data by pet_id:
        - Creates new pet
        - Retrieves pet data and asserts retrieved data corresponds to expected
        - Cleans up the pet
        """
        pet_id = create_pet["id"]
        cleanup_pet.append(pet_id)

        pet_service.get_pet_and_assert(pet_id, create_pet, assert_response_full)

    @allure.title(
        "Error 404 is displayed on attempt to retrieve pet using invalid pet id"
    )
    @pytest.mark.parametrize(
        "pet_id, message, key_type, code",
        [
            (7777, "Pet not found", "error", 1),
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
    def test_find_pet_by_invalid_id(self, pet_id, message, key_type, code, pet_service):
        """
        Tests negative scenarios (get pet by invalid pet_id):
        - not existing
        - invalid type
        - special characters
        """
        response = pet_service.get_pet_by_id(pet_id)

        assert_response_code(response, 404)

        pet_data = response.json()
        assert pet_data["message"] == message, 'Unexpected "message" key value'
        assert pet_data["code"] == code, 'Unexpected "code" key value'
        assert pet_data["type"] == key_type, 'Unexpected "type" key value'

    @allure.title(
        "Error 405 is displayed on attempt to retrieve pet using empty pet id"
    )
    def test_find_pet_with_empty_id(self, pet_service):
        """
        Tests negative scenario (empty pet_id)
        """
        response = pet_service.get_pet_by_id("")

        assert_response_code(response, 405)
