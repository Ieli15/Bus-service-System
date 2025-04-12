from marshmallow import Schema, fields

class ScheduleSchema(Schema):
    id = fields.Int(dump_only=True)
    route_id = fields.Int(required=True)
    bus_id = fields.Int(required=True)
    departure_time = fields.DateTime(required=True)
    arrival_time = fields.DateTime(required=True)
