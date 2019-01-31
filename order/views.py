from aiohttp import web
import asyncio
from ws.handler import send_to_ws
from models.auth import User


loop = asyncio.get_event_loop()


async def after_5():
    await asyncio.sleep(5)
    await User.create(name='User name', password='123456', phone="1234567")


class OrderView(web.View):

    async def get(self):
        loop.create_task(send_to_ws('Websocket handling from http view'))
        loop.create_task(after_5())  # doing many process without blocking response
        return web.json_response({'hello': 'World AioHttp'})

    async def post(self):
        data = await self.request.post()
        return web.json_response(["Handle post request"])
