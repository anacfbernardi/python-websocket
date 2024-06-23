from typing import Dict

from websockets.sync.client import connect

from src.aggregators.aggregators_list import aggregators
from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error


class AddTradingAggregator(BaseCommand):
    """
    TB should be able to receive the clear prices message from connected Consumers in the same format described in the TA section.
    After the clear prices message, any message received for any symbol should be considered a message with the latest price.
    """

    async def process_data_received(self) -> Dict:
        if "host" not in self._data_received:
            return return_default_error()

        host = self._data_received["host"]
        try:
            await aggregators.add_aggregator(host)
            return {"status": "processed", "message": f"connected to {host}"}
        except Exception as e:
            print(e)
            return {"status": "not processed", "message": f"error connecting to {host}"}
