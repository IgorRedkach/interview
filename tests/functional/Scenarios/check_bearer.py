from tests.functional.fixtures.steps import *
from pytest_bdd import when, scenario, parsers
import json

# to do:
# @pytest.mark.parametrize(
#     ["bearer"],
#     [("test")],
# )


@scenario('../features/sample.feature', 'check Bearer')
def test_check_bearer():
    pass


@then('Tokens are the same')
def compare_tokens(bearer, get_response):
    content = json.loads(get_response.content)
    assert content['authenticated']
    assert content['token'] == bearer

