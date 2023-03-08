import pytest

from src.baseclasses.response import Response
from src.schemas.user import User
from src.generators.player_localization import PlayerLocalization


@pytest.mark.skip
def test_getting_users_list(test_response):
    """Test status 200 and data is valid."""
    Response(test_response).assert_status_code(200).validate(User)


@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE',
    'MERGED'
])
def test_player_status(status, get_player_generator):
    print(get_player_generator.set_account_status(status).build())


@pytest.mark.parametrize('balance', [
    '100',
    '0',
    '-100',
    'abc'
])
def test_player_balance(balance, get_player_generator):
    print(get_player_generator.set_balance(balance).build())


@pytest.mark.parametrize('deleted_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_player_not_all_data(deleted_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[deleted_key]
    print(object_to_send)


@pytest.mark.parametrize('localization', [
    'es_ES',
    'fr_FR',
    'zh_CN',
    'uk_UA'
])
def test_player_localization(localization, get_player_generator):
    print(get_player_generator.update_inner_generator('localize', PlayerLocalization(localization).set_number(15)).build())
