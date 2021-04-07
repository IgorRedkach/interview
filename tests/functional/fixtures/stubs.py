import pytest


@pytest.fixture
def bearer():
    return 'test'

@pytest.fixture
def url():
    return "http://httpbin.org/"