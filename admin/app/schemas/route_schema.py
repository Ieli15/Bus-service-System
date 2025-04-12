from marshmallow import Schema, fields

class RouteSchema(Schema):
    id = fields.Int(dump_only=True)
    source = fields.Str(required=True)
    destination = fields.Str(required=True)
    distance = fields.Float(required=True)
