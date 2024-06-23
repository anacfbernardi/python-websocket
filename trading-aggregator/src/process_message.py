import json

from src.commands.command_resolver import ResolveCommands
from src.commons.default_error_message import return_default_error


async def process_message_data(data: str) -> dict:
    try:
        data_received = await __validate_message_received(data)
        return await ResolveCommands.resolve_commands(data_received)
    except Exception as e:
        return return_default_error()


async def __validate_message_received(data_received: str) -> dict:
    data_received = json.loads(data_received)

    if "action" not in data_received:
        raise

    return data_received
