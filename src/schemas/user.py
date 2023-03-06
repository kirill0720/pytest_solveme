from pydantic import BaseModel, validator

from src.enums.user_enums import Genders, Statuses, UserError


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_email_contains_dog(cls, email):
        if '@' not in email:
            raise ValueError(UserError.WRONG_EMAIL.value)

        return email

# z = {
#     'id': 840813,
#     'name': 'Udit Rana DDS',
#     'email': 'udit_rana_dds@schuster-von.org',
#     'gender': 'male',
#      'status': 'inactive'
# }
