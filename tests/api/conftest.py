import os

import pytest

from core.api.utils import load_json_config
from services import PetService, StoreService, UserService

current_dir = os.path.dirname(os.path.abspath(__file__))
body_config = load_json_config(os.path.join(current_dir, 'config/request_bodies.json'))


@pytest.fixture
def pet_service():
    headers = load_json_config('config/headers.json')["default"]
    return PetService(headers)


@pytest.fixture
def store_service():
    headers = load_json_config('config/headers.json')["default"]
    return StoreService(headers)


@pytest.fixture
def user_service():
    headers = load_json_config('config/headers.json')["default"]
    return UserService(headers)


@pytest.fixture
def create_pet(pet_service):
    body = body_config["add_available_pet_with_all_parameters"]

    response = pet_service.add_pet(body)
    assert response.status_code == 200, f"Failed to create pet: {response.status_code}"

    pet_data = response.json()

    return pet_data


@pytest.fixture
def cleanup_pet(pet_service):
    pet_ids = []

    yield pet_ids

    for pet_id in pet_ids:
        response = pet_service.delete_pet(pet_id)
        assert response.status_code == 200, f"Failed to delete pet ID {pet_id}"


@pytest.fixture
def place_order(store_service):
    body = body_config["place_order_for_purchasing_pet"]

    response = store_service.place_order(body)
    assert response.status_code == 200, f"Failed to place order: {response.status_code}"

    order_data = response.json()

    return order_data


@pytest.fixture
def create_user(user_service):
    body = body_config["add_single_user"]

    response = user_service.create_with_list(body)
    assert response.status_code == 200, f"Failed to create user: {response.status_code}"

    user_data = response.json()

    return user_data


@pytest.fixture
def cleanup_user(user_service):
    users = []

    yield users

    for username in users:
        response = user_service.delete_user(username)
        assert response.status_code == 200, f"Failed to delete user {username}"
