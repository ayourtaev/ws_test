import ssl
import asyncio
import websockets

ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
ssl_context.load_verify_locations('super-site.com.cert')


async def hello(uri):
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        await websocket.send('{"up_id":322}')
        greeting = await  websocket.recv()
        print('< {}'.format(greeting))


loop = asyncio.get_event_loop()
loop.run_until_complete(hello('wss://dev-onli.getpackage.com'))
