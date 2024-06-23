from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error
from src.services.storage_api_service import clear_prices as clear_prices_from_api


class ClearPrices(BaseCommand):
    """
    It should clear all the prices stored in the Storage API.
    After the clear prices message, any message received for each symbol should be considered a message with latest price.
    More info about the endpoints for the storage API will be described in the Storage API section.

    The message to clear all the prices from the storage API should have the following format:
        { "action": "clear-prices" }
    And the app should reply with the status of success after clearing it from the API.
        { "status": "processed" }
    """

    async def process_data_received(self) -> dict:
        try:
            await clear_prices_from_api()
            return {"status": "processed"}
        except Exception as e:
            print(e)
            return return_default_error()
