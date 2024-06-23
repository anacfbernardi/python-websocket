from typing import List


class Connections:
    _instance = None
    _connections = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Connections, cls).__new__(cls)
            cls._connections = set()
        return cls._instance

    async def add_connection(self, ws):
        self._connections.add(ws)

    def get_connections(self):
        return self._connections


connections = Connections()
