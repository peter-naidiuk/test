from marshmallow import Schema, fields


class TaskCreateSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
