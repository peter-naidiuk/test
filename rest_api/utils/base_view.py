import json
import time
from http import HTTPStatus

from flask.views import MethodView
from marshmallow import ValidationError

from rest_api.utils.serializer import JSONSerializer
from .exceptions import BadRequest


class BaseView(MethodView):

    @staticmethod
    def get_response(data, status=HTTPStatus.OK):
        return json.dumps(
            {
                "status": status,
                "data": data,
                "timestamp": time.time()
            },
            cls=JSONSerializer
        )

    @staticmethod
    def validate_request(data, validator):
        try:
            data = validator().load(data)
        except ValidationError as e:
            raise BadRequest(e)
        return data
