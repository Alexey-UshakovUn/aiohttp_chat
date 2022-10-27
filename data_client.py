from dataclasses import dataclass
import websockets


@dataclass()
class Client:
    name: str
    client_socket: websockets.WebSocketClientProtocol
