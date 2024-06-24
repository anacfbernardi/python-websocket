from src.commands.base_command import BaseCommand
from src.commons.default_error_message import return_default_error
from src.providers.providers_controller import providers


class AddProvider(BaseCommand):
    """
    The message should be in JSON format.
    It should require the add-provider action, the URL of the data provider,
        and the list of symbols that the TA should handle from this data provider.
    If the list of symbols is empty, the TA should ignore all symbols.
    """

    async def process_data_received(self) -> dict:
        try:
            if "host" not in self._data_received or "symbols" not in self._data_received:
                raise

            await providers.add_provider(self._data_received["host"], self._data_received["symbols"])
            return {"status": "processed"}
        except Exception as e:
            print(e)
            return return_default_error()
