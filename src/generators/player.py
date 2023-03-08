from src.enums.user_enums import Statuses
from src.generators.player_localization import PlayerLocalization


class Player:
    def __init__(self):
        self.result = {}
        self.reset()

    def set_account_status(self, status=Statuses.ACTIVE.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar='https://google.com'):
        self.result['avatar'] = avatar
        return self

    def reset(self):
        self.set_account_status()
        self.set_balance()
        self.set_avatar()
        self.result['localize'] = {
            'en': PlayerLocalization('en_US').build(),
            'ru': PlayerLocalization('ru_RU').build()
        }
        return self

    def build(self):
        """Returns object as JSON."""
        return self.result
