import json
from json import JSONEncoder

from sqlalchemy.engine import ResultProxy
from sqlalchemy.ext.declarative import DeclarativeMeta


class JSONSerializer(JSONEncoder):

    @staticmethod
    def _serialize_object(obj):
        fields = {}
        obj_dict = obj.__dict__
        for field in obj.__table__.columns.keys():
            data = obj_dict.get(field)
            try:
                json.dumps(data)
                fields[field] = data
            except TypeError:
                fields[field] = None
        return fields

    def default(self, obj):
        if isinstance(obj, ResultProxy):
            return [dict(item) for item in obj]
        if isinstance(obj.__class__, DeclarativeMeta):
            return JSONSerializer._serialize_object(obj)
        return JSONEncoder.default(self, obj)
