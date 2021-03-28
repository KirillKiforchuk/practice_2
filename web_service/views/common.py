from aiohttp import web
from aiohttp_apispec import request_schema, response_schema

from ..schemas.common import FreeTextHandler, PingResponse


async def index_handler(_):
    raise web.HTTPFound('/swagger')


@response_schema(PingResponse)
async def ping_handler(_):
    return web.json_response({'ping': 'pong'})


@request_schema(FreeTextHandler)
async def free_text_handler(request):
    request_body = await request.json()
    request_text = request_body['text']

    # TODO: implement your handler logic here, for example:
    if 'abcd' in request_text:
        raise web.HTTPBadRequest(
            reason='Your request  shouldn\'t contain "abcd"'
        )

    return web.json_response({'status': 'ok'})
