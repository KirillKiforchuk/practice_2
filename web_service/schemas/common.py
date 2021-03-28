from marshmallow import fields, Schema


class PingResponse(Schema):
    ping = fields.Str(
        description='Health check response',
        example='pong'
    )


class FreeTextHandler(Schema):
    text = fields.Str(
        description='Free text input',
        example='Some free text input',
        required=True
    )
