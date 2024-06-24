from typing import Dict

from websockets.sync.client import connect

from src.aggregators.aggregators_controller import aggregators
from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error


class Unsubscribe(BaseCommand):

    async def process_data_received(self) -> Dict:
        return return_default_error()
