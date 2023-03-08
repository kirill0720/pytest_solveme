import pytest
import requests

from configuration import SERVICE_URL
from src.generators.player import Player


@pytest.fixture
def test_response():
    return requests.get(SERVICE_URL)


@pytest.fixture
def get_player_generator():
    return Player()
