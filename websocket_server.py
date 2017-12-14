import asyncio
import websockets


async def hello(websocket, path):
    # Here’s a WebSocket server example. It reads a name from the client,
    # sends a greeting, and closes the connection.
    name = await websocket.recv()
    print('< {}'.format(name))

    greeting = 'Hello {}!'.format(name)
    await  websocket.send(greeting)
    print('> {}'.format(greeting))


if __name__ == '__main__':
    print('Hello im ws server')
    start_server = websockets.serve(hello, 'localhost', 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
