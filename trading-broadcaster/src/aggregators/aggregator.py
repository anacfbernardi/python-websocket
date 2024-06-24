import asyncio

from websockets import ConnectionClosed
from websockets.client import connect


class Aggregator:
    url: str
    connection: any
    providers_count: int
    task: any

    def __init__(self, url):
        self.url = url
        self.listener = None
        self.sender = None
        self.providers_count = 0

    def inc_providers_count(self):
        self.providers_count += 1

    def clear_providers_count(self):
        self.providers_count = 0

    async def start_listening_aggregator(self):
        self.listener = await connect(self.url)
        self.sender = await connect(self.url)
        self.task = asyncio.create_task(self.__listen_to_aggregator(), name=self.url)

    async def stop_listening_aggregator(self):
        await self.listener.close()
        await self.sender.close()

    async def __listen_to_aggregator(self):
        try:
            while self.listener.open:
                data = await self.listener.recv()
                print(data)
        except ConnectionClosed:
            await self.stop_listening_aggregator()

    async def send_message_to_aggregator(self, message: str) -> str:
        if self.sender.open:
            await self.sender.send(message)
            message = await self.sender.recv()
            self.sender.messages.clear()
            return message
