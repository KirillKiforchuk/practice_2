from aiohttp import web
from aiohttp_apispec import response_schema

from ..schemas.common import PingResponse


async def index_handler(_):
    raise web.HTTPFound('/swagger')


@response_schema(PingResponse)
async def ping_handler(_):
    return web.json_response({'ping': 'pong'})
