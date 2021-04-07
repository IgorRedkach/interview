from tests.functional.fixtures.steps import *
from pytest_bdd import when, scenario, parsers
import json


@scenario('../features/sample.feature', 'check UUID')
def test_check_uuid():
    pass


@then('UUID are not empty')
def compare_tokens(bearer, get_response):
    content = json.loads(get_response.content)
    assert content['uuid']
