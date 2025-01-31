import allure


@allure.step("Assert response with minimal set of parameters provided in request body")
def assert_response_min(pet_data, body_req):
    assert pet_data["id"] == body_req["id"], "Unexpected 'id' value"
    assert pet_data["name"] == body_req["name"], "Unexpected 'name' value"
    assert (
        pet_data["photoUrls"] == body_req["photoUrls"]
    ), "Unexpected 'photoUrls' value"
    assert "tags" in pet_data.keys(), '"tags" key is missing in the response'


@allure.step("Assert response with full set of parameters provided in request body")
def assert_response_full(data, body_req):
    if isinstance(body_req, list) and len(body_req) == 1:
        body_req = body_req[0]
    assert data == body_req, "Response data does not match expected data"


@allure.step("Assert response code")
def assert_response_code(response, code=200):
    assert (
        response.status_code == code
    ), f"Expected code = {code}, got {response.status_code}"


@allure.step("Assert response for 'Create list of users with given array' endpoint")
def assert_user_list_created_response(user_data):
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
def assert_user_updated_response(user_data, body_req):
    assert (
        user_data["code"] == 200
    ), f"Expected 'code' == 200, Actual - {user_data["code"]}"
    assert (
        user_data["type"] == "unknown"
    ), f"Expected 'type' == 'unknown', Actual - {user_data["type"]}"
    assert user_data["message"] == str(
        body_req["id"]
    ), "Unexpected 'message' value, 'message' should be equal to user id"
