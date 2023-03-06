from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.status_code = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema(self.response_json)

        return self

    def assert_status_code(self, status_code: int | list):
        if isinstance(status_code, list):
            assert self.status_code in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value

        return self
