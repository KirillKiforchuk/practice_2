from marshmallow import fields, Schema


class PingResponse(Schema):
    ping = fields.Str(
        description='Health check response',
        example='pong'
    )
