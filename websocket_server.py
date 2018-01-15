import ssl
import asyncio
import websockets


async def hello(websocket, path):
    name = await websocket.recv()
    print("< {}".format(name))

    greeting = "Hello {}!".format(name)
    await websocket.send(greeting)
    print("> {}".format(greeting))

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.check_hostname = False
ssl_context.load_cert_chain('super-site.com.cert', 'super-site.com.key')

start_server = websockets.serve(hello, 'localhost', 8999, ssl=ssl_context)

loop = asyncio.get_event_loop()
print('>>> RUN <<<')
loop.run_until_complete(start_server)

try:
    loop.run_forever()
except KeyboardInterrupt as e:
    loop.run_until_complete(start_server.wait_closed())
finally:
    loop.close()
