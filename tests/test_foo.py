import pytest

from src.baseclasses.response import Response
from src.schemas.user import User


@pytest.mark.development
def test_getting_users_list(test_response):
    """Test status 200 and data is valid."""
    Response(test_response).assert_status_code(200).validate(User)
