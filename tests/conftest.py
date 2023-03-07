import pytest
import requests

from configuration import SERVICE_URL


@pytest.fixture
def test_response():
    return requests.get(SERVICE_URL)