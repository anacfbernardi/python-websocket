from websockets.client import connect

from src.subscribers.subscriber_type import SubscriberType


class Subscribers:
    path: str
    ws: any
    subscriber_type: SubscriberType
    connection: any

    def __init__(self, path: str, subscriber_type: SubscriberType, ws: any):
        self.path = path
        self.subscriber_type = subscriber_type
        self.ws = ws

    @classmethod
    async def create(cls, path: str, subscriber_type: SubscriberType, ws: any):
        instance = cls(path, subscriber_type, ws)
        return instance

    async def unsubscribe(self):
        await self.connection.close()

    async def send_message_to_subscriber(self):
        if self.ws.open:
            await self.ws.send(message)
            message = await self.ws.recv()
            self.ws.messages.clear()
            return message

    def get_path_from_ws(self):
        return self.ws
