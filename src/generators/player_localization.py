from faker import Faker


class PlayerLocalization:
    def __init__(self, language):
        self.fake = Faker(language)
        self.result = {'nickname': self.fake.first_name()}

    def build(self):
        """Returns object as JSON."""
        return self.result
