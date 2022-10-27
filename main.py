import websockets
import asyncio

all_clients = []


async def send_message(message: str):
    for client in all_clients:
        await client.send(message)


async def new_client_connected(client_socket: websockets.WebSocketClientProtocol, path: str):
    print('New client connected', path)
    all_clients.append(client_socket)
    await message_recv(client_socket)


async def message_recv(client_socket: websockets.WebSocketClientProtocol):
    while True:
        new_message = await client_socket.recv()
        print('data from client', new_message)
        await send_message(message=new_message)


async def start_server() -> None:
    await websockets.serve(new_client_connected, 'localhost', 8888)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()
