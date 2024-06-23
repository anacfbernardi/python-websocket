
from os import getenv
import asyncio
import json
from dotenv import load_dotenv
import time
import websockets
from _ import _

_._()
load_dotenv()

##################################################
## PLEASE DO NOT MODIFY, RENAME OR REMOVE ANY OF THE CODE ABOVE. 
## YOU CAN ADD YOUR OWN CODE TO THIS FILE OR MODIFY THE CODE BELOW TO CHANGE THE MESSAGES SENT FROM THE DATA PROVIDER.
##################################################


CONNECTIONS = set()
data_provider_server = None


messagesConfig = {
  'timeToWaitBeforeSendingFirstMessage': 1000,
  'timeToWaitBeforeSendingNewMessage': 60,
  'numberOfIterations': 1,
  'messages': [
      {
        'symbol': 'a631dc6c-ee85-458d-80d7-50018aedfbad',
        'price': 10.58,
        'quantity': 500,
        'timestampDifference': 0
      },
      {
        'symbol': '9e8bff74-50cd-4d80-900c-b5ce3bf371ee',
        'price': 18.58,
        'quantity': 1500,
        'timestampDifference': 1
      },
      {
        'symbol': 'a631dc6c-ee85-458d-80d7-50018aedfbad',
        'price': 11.0,
        'quantity': 1000,
        'timestampDifference': -500
      },
      {
        'symbol': 'a631dc6c-ee85-458d-80d7-50018aedfbad',
        'price': 15.0,
        'quantity': 500,
        'timestampDifference': 2
      },
      {
        'symbol': '4',
        'price': 9.0,
        'quantity': 1000,
        'timestampDifference': 3
      },
    ]
}


async def main():
    global data_provider_server
    try:
        port = int(getenv('WS_DATA_PROVIDER_PORT', 9001))
        data_provider_server = await configure_data_provider(port)
        await asyncio.Future()  # run forever
    except Exception as e:
        if data_provider_server:
            await data_provider_server.close()
        print(e)


async def configure_data_provider(port):
    server = await websockets.serve(handler, "127.0.0.1", port)
    print(f"server listening on port {port}")
    return server


async def send_data():
    messages_to_send = messagesConfig["messages"]
    now = int(time.time() * 1000)
    for index in range(len(messages_to_send) * messagesConfig["numberOfIterations"]):
        if index % len(messages_to_send) == 0:
            now = int(time.time() * 1000)
        data = messages_to_send[index % len(messages_to_send)]
        data_to_send = {
            "symbol": data["symbol"],
            "price": data["price"],
            "quantity": data["quantity"],
            "timestamp": now + data["timestampDifference"]
        }
        await dispatch_message_to_all_clients(data_to_send)
        print("message sent: ", data_to_send, int(time.time() * 1000))
        await asyncio.sleep(messagesConfig["timeToWaitBeforeSendingNewMessage"]/1000)


async def dispatch_message_to_all_clients(message):
    for connection in CONNECTIONS:
        await connection.send(json.dumps(message))


async def handler(ws, path):
    try:
        print("client connected")
        CONNECTIONS.add(ws)

        if messagesConfig:
            while True:
                await asyncio.sleep((messagesConfig["timeToWaitBeforeSendingFirstMessage"] or 5000) / 1000)
                await send_data()
                print('finished sending data')
                print(f'will send again in {messagesConfig["timeToWaitBeforeSendingNewMessage"] or 5000} seconds')
                await asyncio.sleep(messagesConfig["timeToWaitBeforeSendingNewMessage"] or 5000)
        async for message in ws:
            try:
                data = json.loads(message)
                print("message received: ", data)
            except Exception as e:
                print(e)
            
    except Exception as e:
        print(e)
    finally:
        await ws.close()
        print("client disconnected")


if __name__ == "__main__":
    asyncio.run(main())
