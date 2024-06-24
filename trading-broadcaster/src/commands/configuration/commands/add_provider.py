import json
import asyncio
from typing import Dict

from websockets.sync.client import connect

from src.aggregators.aggregators_list import aggregators
from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error


class AddProvider(BaseCommand):
    """
    TB should be able to receive the clear prices message from connected Consumers
        in the same format described in the TA section.
    After the clear prices message, any message received for any symbol
        should be considered a message with the latest price.
    """

    async def process_data_received(self) -> Dict:
        if "host" not in self._data_received:
            return return_default_error()

        aggregator = aggregators.get_aggregator_with_min_providers_count()

        if aggregator is None:
            return return_default_error()

        try:
            if aggregator.sender.open:
                await aggregator.sender.send(json.dumps(self._data_received))
                message = await aggregator.sender.recv()
                aggregator.inc_providers_count()
                print(f"Received: {message}")                
                return json.loads(message)
        except Exception as e:
            print(e)
            return return_default_error()
