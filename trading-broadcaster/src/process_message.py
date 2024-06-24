import json

from src.commands.commands_resolver import ResolveCommands
from src.commons.default_error_message import return_default_error


async def process_message_data(data: str, path: str, ws: any) -> dict:
    try:
        data_received = await __validate_message_received(data)
        return await ResolveCommands.resolve_commands(data_received, path, ws)
    except Exception as e:
        return return_default_error()


async def __validate_message_received(data_received: str) -> dict:
    data_received = json.loads(data_received)

    if "action" not in data_received:
        return return_default_error()

    return data_received
