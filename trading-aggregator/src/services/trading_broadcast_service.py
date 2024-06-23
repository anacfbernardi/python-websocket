import json

from src.services.connections_manager import connections
from src.services.storage_api_service import create_prices, get_price_from_symbol
from src.symbols.symbols_manager import get_symbols


async def send_message_to_trading_broadcast(message):
    if not await should_send_symbol(message):
        return

    try:
        for connection in connections.get_connections():
            if connection.open:
                prices_list = await TradindBroadcastService.build_message_to_trading_broadcast(message)
                await connection.send(json.dumps(prices_list))
    except Exception as e:
        print(f"Error sending message to tragind broadcast: {e}")


async def should_send_symbol(message):
    try:
        message_data = json.loads(message)
        return message_data["symbol"] in await get_symbols()
    except:
        return False


class TradindBroadcastService:

    async def __create_price(self, message):
        message_data = json.loads(message)

        payload = {
            "price": message_data["price"],
            "quantity": message_data["quantity"],
            "timestamp": message_data["timestamp"],
        }

        await create_prices(message_data["symbol"], payload)

    async def __get_all_latest_filtered(self):
        all_prices = []

        for symbols in await get_symbols():
            try:
                price = await get_price_from_symbol(symbols)
                all_prices.append(price.json())
            except Exception as e:
                print(e)

        return all_prices

    @staticmethod
    async def build_message_to_trading_broadcast(message):
        service = TradindBroadcastService()

        await service.__create_price(message)
        return await service.__get_all_latest_filtered()
