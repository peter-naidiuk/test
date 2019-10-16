from marshmallow import Schema, fields


class TaskPatchSchema(Schema):
    finished = fields.Bool(required=True)


class TaskEditSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    finished = fields.Bool()
