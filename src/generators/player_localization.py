from faker import Faker


class PlayerLocalization:
    def __init__(self, language):
        self.fake = Faker(language)
        self.result = {'nickname': self.fake.first_name()}

    def set_number(self, number=10):
        self.result['number'] = number
        return self

    def build(self):
        """Returns object as JSON."""
        return self.result
