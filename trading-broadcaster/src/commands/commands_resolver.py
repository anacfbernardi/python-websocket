from src.commands.configuration.commands import (
    AddProvider,
    AddTradingAggregator,
    ClearPrices,
    ClearProviders,
    ClearTradingAggregators,
)
from src.commands.configuration.configuration_commands_type import ConfigurationCommandsType
from src.commands.data.commands import Subscribe, Unsubscribe
from src.commands.data.data_commands_type import DataCommandsType
from src.commons.default_error_message import return_default_error


class ResolveCommands:
    __ACTION_MAP = {
        ConfigurationCommandsType.ADD_TRADING_AGGREGATOR.value: AddTradingAggregator,
        ConfigurationCommandsType.CLEAR_TRADING_AGGREGATORS.value: ClearTradingAggregators,
        ConfigurationCommandsType.ADD_PROVIDER.value: AddProvider,
        ConfigurationCommandsType.CLEAR_PROVIDERS.value: ClearProviders,
        ConfigurationCommandsType.CLEAR_PRICES.value: ClearPrices,
        DataCommandsType.SUBSCRIBE.value: Subscribe,
        DataCommandsType.UNSUBSCRIBE.value: Unsubscribe,
    }

    def __get_command(self, action: str):
        return self.__ACTION_MAP[action]

    @staticmethod
    async def resolve_commands(data_received: dict, path: str, ws: any):
        try:
            resolve = ResolveCommands()
            command = resolve.__get_command(data_received["action"])
            return await command(data_received).process_data_received()
        except Exception as e:
            return return_default_error()
