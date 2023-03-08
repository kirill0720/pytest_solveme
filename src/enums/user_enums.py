from enum import Enum


class Genders(Enum):
    FEMALE = 'female'
    MALE = 'male'


class Statuses(Enum):
    ACTIVE = 'ACTIVE'
    BANNED = 'BANNED'
    DELETED = 'DELETED'
    INACTIVE = 'INACTIVE'
    MERGED = 'MERGED'


class UserError(Enum):
    WRONG_EMAIL = 'Email does not contain @.'
