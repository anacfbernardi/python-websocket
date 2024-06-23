import asyncio
import json
import os

import websockets
from dotenv import load_dotenv

from src.process_message import process_message_data
from src.services.connections_manager import connections

load_dotenv()


async def main():
    try:
        trading_aggregator_server = await create_trading_aggregator_server()
        await asyncio.Future()  # run forever
    except Exception as e:
        if trading_aggregator_server:
            await trading_aggregator_server.close()
        print(e)


async def create_trading_aggregator_server():
    port = int(os.getenv("WS_CONSUMER_PORT", 9100))
    trading_aggregator_server = await websockets.serve(handler, "127.0.0.1", port)
    print(f"server listening on port {port}")
    return trading_aggregator_server


async def handler(ws, path):
    try:
        await connections.add_connection(ws)
        print("client connected")

        async for message in ws:
            try:
                data = await process_message_data(message)
                await ws.send(json.dumps(data))
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)

    finally:
        await ws.close()
        print("client disconnected")


if __name__ == "__main__":
    asyncio.run(main())
