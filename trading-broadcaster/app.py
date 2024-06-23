import asyncio
import json
import os

import websockets
from dotenv import load_dotenv

from src.process_message import process_message_data

load_dotenv()


async def main():
    try:
        trading_broadcaster_server = await create_trading_broadcaster_server()
        await asyncio.Future()  # run forever
    except Exception as e:
        if trading_broadcaster_server:
            await trading_broadcaster_server.close()
        print(e)


async def create_trading_broadcaster_server():
    port = int(os.getenv("WS_CONSUMER_PORT", 9000))
    trading_broadcaster_server = await websockets.serve(handler, "127.0.0.1", port)
    print(f"server listening on port {port}")
    return trading_broadcaster_server


async def handler(ws, path):
    try:
        print("client connected")

        async for message in ws:
            try:
                data = await process_message_data(message)
                print("message received: ", data)
                await ws.send(json.dumps(data))
            except Exception as e:
                print(e)
                await ws.send(json.dumps(e))

    except Exception as e:
        print(e)

    finally:
        await ws.close()
        print("client disconnected")


if __name__ == "__main__":
    asyncio.run(main())
