"""Common steps."""

import requests
import json
from urllib.parse import urljoin
from urllib.parse import urlparse
from tests.functional.fixtures.stubs import *
from pytest_bdd import given, when, then, parsers


@then(parsers.parse('status code is {status_code:d}'))
def status_code_is_200(status_code, get_response):
    assert status_code == get_response.status_code


@given(parsers.parse('I do GET from /{path:w}'), target_fixture='get_response')
def post_pet(bearer, path, url):
    payload = {}
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + bearer
    }
    return requests.request("GET", urljoin(url, path), headers=headers, data=payload)

