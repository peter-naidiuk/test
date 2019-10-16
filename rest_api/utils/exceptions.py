from http import HTTPStatus


class BaseApplicationException(Exception):
    _status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args):
        super().__init__(*args)
        self.status = self._status


class BadRequest(BaseApplicationException):
    _status = HTTPStatus.BAD_REQUEST
