import asyncio

from websockets import ConnectionClosed
from websockets.client import connect

class Aggregator:
    url: str
    connection: any
    providers_count: int

    def __init__(self, url):
        self.url = url
        self.connection = None
        self.providers_count = 0
        
    def inc_providers_count(self):
        self.providers_count += 1

    def clear_providers_count(self):
        self.providers_count = 0
    
    async def start_listening_aggregator(self):
        self.connection = await connect(self.url)
        asyncio.get_event_loop().create_task(self.__listen_to_aggregator())

    async def stop_listening_aggregator(self):
        await self.connection.close()
        
    async def __listen_to_aggregator(self):
        try:
            while self.connection.open:
                data = await self.connection.recv()
                print(data)
        except ConnectionClosed:
            await self.stop_listening_aggregator()

