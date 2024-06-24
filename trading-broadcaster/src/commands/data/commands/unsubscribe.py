from typing import Dict

from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error
from src.subscribers.subscribers_controller import subscribers


class Unsubscribe(BaseCommand):

    async def process_data_received(self) -> Dict:
        try:
            await subscribers.remove_subscriber(self._path)
            return {"status": "processed"}
        except Exception as e:
            print(e)
            return return_default_error()
