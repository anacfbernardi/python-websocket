import json
from typing import Dict

from websockets.sync.client import connect

from src.aggregators.aggregators_controller import aggregators
from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error


class ClearTradingAggregators(BaseCommand):
    """
    The app should also support the option to clear all Trading Aggregators.
    This option should disconnect the Trading Broadcaster from all Trading Aggregators.
    Before disconnecting, the Trading Broadcaster should also send the message for the connected Trading Aggregators
        to disconnect from the Data Providers that they are connected to.
    The message to clear the Trading Aggregators and consequently the Data Providers should be in the following format:
        { "action": "clear-trading-aggregators" }

    The response should be "processed" or "not processed":
        { "status": "processed" }
    """

    async def process_data_received(self) -> Dict:
        aggregators_list = aggregators.get_aggregators()

        if not len(aggregators_list):
            return return_default_error()

        try:
            
            for aggregator in aggregators_list:
                try:
                    message = await aggregator.send_message_to_aggregator(json.dumps({"action": "clear-providers"}))
                    await aggregators.remove_aggregator(aggregator.url)
                    print(f"Received: {message}")
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
            return return_default_error()

        return {"status": "processed"}
