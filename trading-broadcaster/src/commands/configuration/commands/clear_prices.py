import json
from typing import Dict

from websockets.sync.client import connect

from src.aggregators.aggregators_list import aggregators
from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error


class ClearPrices(BaseCommand):
    """
    TB should be able to receive the clear prices message from
        connected Consumers in the same format described in the TA section.
    After the clear prices message, any message received for
        any symbol should be considered a message with the latest price.
    """

    async def process_data_received(self) -> Dict:
        aggregators_list = aggregators.get_aggregators()

        if not len(aggregators_list):
            return return_default_error()

        for aggregator in aggregators_list:
            with connect(aggregator.url) as websocket:
                data_string = json.dumps(self._data_received)
                try:
                    websocket.send(data_string)
                    message = await websocket.recv()
                    print(f"Received: {message}")
                except Exception as e:
                    print(e)

        return {"status": "Processed"}
