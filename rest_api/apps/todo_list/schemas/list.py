from marshmallow import Schema, fields


class ListCreateSchema(Schema):
    name = fields.Str(required=True)
