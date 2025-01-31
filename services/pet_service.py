import allure

from core import BaseService, assert_response_code


class PetService(BaseService):

    def __init__(self, headers):
        super().__init__()
        self.BASE_URL = "https://petstore.swagger.io/v2/pet"
        self.headers = headers

    @staticmethod
    def _check_response(response):
        if response.headers.get("Content-Type") != "application/json":
            raise ValueError(
                f'Invalid Content-Type: {response.headers.get("Content-Type")}'
            )
        return response

    @allure.step("Get pet by ID")
    def get_pet_by_id(self, pet_id):
        response = self.get(f"{self.BASE_URL}/{pet_id}", headers=self.headers)
        self._check_response(response)
        return response

    @allure.step("Add new pet")
    def add_pet(self, pet_data):
        response = self.post(f"{self.BASE_URL}", headers=self.headers, json=pet_data)
        self._check_response(response)
        return response

    @allure.step("Delete pet by ID")
    def delete_pet(self, pet_id):
        response = self.get(f"{self.BASE_URL}/{pet_id}", headers=self.headers)
        self._check_response(response)
        return response

    @allure.step("Add new pet and verify response code and body")
    def add_pet_and_assert(self, body_req, assertion):
        response = self.add_pet(body_req)
        assert_response_code(response)

        pet_data = response.json()
        assertion(pet_data, body_req)

    @allure.step("Add pet by ID and verify response code and body")
    def get_pet_and_assert(self, pet_id, body_req, assertion):
        response = self.get_pet_by_id(pet_id)
        assert_response_code(response)

        pet_data = response.json()
        assertion(pet_data, body_req)
