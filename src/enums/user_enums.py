from enum import Enum


class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(Enum):
    active = 'active'
    inactive = 'inactive'


class UserError(Enum):
    WRONG_EMAIL = 'Email does not contain @.'
