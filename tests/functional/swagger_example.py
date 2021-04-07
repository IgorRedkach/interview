import schemathesis
from hypothesis import settings
from schemathesis.checks import not_a_server_error

schema = schemathesis.from_uri("https://petstore.swagger.io/v2/swagger.json")


@schema.parametrize(method="GET", endpoint="/pet")
@settings(max_examples=25)
def test_get_booking(case):
    response = case.call()
    # assert response.status_code < 500
    case.validate_response(response, checks=(not_a_server_error,))
