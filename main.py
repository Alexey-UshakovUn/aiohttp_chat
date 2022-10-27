import websockets
import asyncio
from data_client import Client

all_clients = []


async def send_message(message: str) -> None:
    for client in all_clients:
        await client.client_socket.send(message)


async def new_client_connected(client_socket: websockets.WebSocketClientProtocol, path: str) -> None:
    print('New client connected', path)
    await client_socket.send('Введите ваше имя!')
    name = await client_socket.recv()
    client = Client(name, client_socket)
    all_clients.append(client)
    await message_recv(client)


async def message_recv(client: Client) -> None:
    while True:
        new_message = await client.client_socket.recv()
        print('data from client', new_message)
        await send_message(message=new_message)


async def start_server() -> None:
    await websockets.serve(new_client_connected, 'localhost', 8888)


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()
