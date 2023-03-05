import requests

from configuration import SERVICE_URL


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200
    print(response.json())