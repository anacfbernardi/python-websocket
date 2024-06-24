from typing import List

from src.subscribers.subscriber_type import SubscriberType
from src.subscribers.subscribers import Subscribers


class SubscriberController:

    _instance = None
    _subscribers = List[Subscribers]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SubscriberController, cls).__new__(cls)
            cls._instance._subscribers = []
        return cls._instance

    async def add_subscriber(self, path: str, type: SubscriberType, ws):
        if not any(a.path == path for a in self._subscribers):
            subscriber = await Subscribers.create(path, type, ws)
            self._subscribers.append(subscriber)

    async def remove_subscriber(self, path):
        subscriber = next((p for p in self._subscribers if p.path == path), None)
        if subscriber is not None:
            await subscriber.unsubscribe()
        self._subscribers = [a for a in self._subscribers if a.path != path]

    def get_subscribers_by_type(self, type: SubscriberType) -> List[Subscribers]:
        return [subscriber for subscriber in self._subscribers if subscriber.subscriber_type == type]

    async def send_message_to_all_subscribers_by_type(self, type: SubscriberType, message):
        for subscriber in self.get_subscribers_by_type(type):
            await subscriber.send_message_to_subscriber(message)


subscribers = SubscriberController()
