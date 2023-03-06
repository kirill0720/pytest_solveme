import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_obj = Response(response)

    test_obj.assert_status_code(200).validate(User)
