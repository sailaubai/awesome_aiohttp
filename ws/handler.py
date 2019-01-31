from aiohttp import web
import aiohttp
import asyncio

ws_listeners = []


async def ws_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    for _ws in ws_listeners:
        _ws.send_str('new joined')
    ws_listeners.append(ws)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                for client in ws_listeners:
                    await client.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws closed {}'.format(ws.exception()))

    ws_listeners.remove(ws)
    print('ws connection closed')
    return ws


async def send_to_ws(data):
    await asyncio.sleep(10)  # imitation process
    for client in ws_listeners:
        await client.send_str(data)
