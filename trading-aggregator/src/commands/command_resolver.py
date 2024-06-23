from src.commands import AddProvider, ClearPrices, ClearProviders, CommandType


class ResolveCommands:
    __ACTION_MAP = {
        CommandType.ADD_PROVIDER.value: AddProvider,
        CommandType.CLEAR_PROVIDERS.value: ClearProviders,
        CommandType.CLEAR_PRICES.value: ClearPrices,
    }

    def __get_command(self, action: str):
        return self.__ACTION_MAP[action]

    @staticmethod
    async def resolve_commands(data_received: dict):
        resolve = ResolveCommands()
        command = resolve.__get_command(data_received["action"])
        return await command(data_received).process_data_received()
