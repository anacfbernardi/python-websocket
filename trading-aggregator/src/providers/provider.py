import asyncio
from typing import List

from websockets import ConnectionClosed
from websockets.client import connect

from src.services.trading_broadcast_service import send_message_to_trading_broadcast


class Provider:
    url: str
    connection: any
    symbols: List

    def __init__(self, url, symbols):
        self.url = url
        self.connection = None
        self.symbols = symbols

    async def start_listening_provider(self):
        self.connection = await connect(self.url)
        print(f"Listening to Provider {self.url}")
        asyncio.get_event_loop().create_task(self.__listen_to_provider(), name=self.url)

    async def stop_listening_provider(self):
        await self.connection.close()
        print(f"Provider {self.url} Connection closed")

    async def __listen_to_provider(self):
        try:
            while self.connection.open:
                data = await self.connection.recv()
                print(data)
                await send_message_to_trading_broadcast(data)
        except ConnectionClosed:
            await self.stop_listening_provider()
