import json
from typing import Dict

from websockets.sync.client import connect

from src.aggregators.aggregators_list import aggregators
from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error


class ClearProviders(BaseCommand):
    """
    The Trading Broadcaster should be able to receive the clear-provider message 
        from the connected Consumers in the same format described in the Clear Providers section for the Trading Aggregator. 
    After receiving this message, the Trading Broadcaster should forward the clear-providers message to all connected Trading Aggregators.
    """

    async def process_data_received(self) -> Dict:
        aggregators_list = aggregators.get_aggregators()

        if len(aggregators_list) == 0:
            return return_default_error()

        for aggregator in aggregators_list:
            with connect(aggregator.url) as websocket:
                data_string = json.dumps(self._data_received)
                try:
                    websocket.send(data_string)
                    message = await websocket.recv()
                    aggregator.clear_providers_count()
                    print(f"Received: {message}")
                except Exception as e:
                    print(e)

        return {"status": "Processed"}
