import allure

from core.api.base_service import BaseService


class APIAssertions(BaseService):

    @allure.step("Assert response with full set of parameters provided in request body")
    def assert_response_full(self, data, body_req):
        if isinstance(body_req, list) and len(body_req) == 1:
            body_req = body_req[0]
        assert data == body_req, "Response data does not match expected data"

    @allure.step("Assert response code")
    def assert_response_code(self, response, code=200):
        assert (
                response.status_code == code
        ), f"Expected code = {code}, got {response.status_code}"
