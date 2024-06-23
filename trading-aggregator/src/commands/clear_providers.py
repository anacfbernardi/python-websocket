from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error
from src.providers.providers_list import providers


class ClearProviders(BaseCommand):
    """
    The app should also support the option to clear all data providers.
    This option will remove and stop listening to all data providers.
    The message to clear the data providers should be in the following format:
    """

    async def process_data_received(self) -> dict:
        try:
            providers_list = providers.get_providers()

            for provider in providers_list:
                await provider.stop_listening_provider()

            providers.clear_providers()
            return {"status": "processed"}
        except Exception as e:
            return return_default_error()
