from typing import Dict

from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error
from src.subscribers.subscriber_type import SubscriberType
from src.subscribers.subscribers_controller import subscribers


class Subscribe(BaseCommand):

    async def process_data_received(self) -> Dict:
        if "channel" not in self._data_received:
            return return_default_error()

        if self._data_received["channel"] not in SubscriberType:
            return return_default_error()

        try:
            await subscribers.add_subscriber(self._path, self._data_received["channel"], self._ws)
            return {"status": "processed"}
        except Exception as e:
            print(e)
            return return_default_error()
