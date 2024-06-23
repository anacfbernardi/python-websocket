import os

import requests
from dotenv import load_dotenv

load_dotenv()


def __get_storage_api_url() -> str:
    port = int(os.getenv("WS_STORAGE_API_PORT", 3000))
    url = os.getenv("WS_STORAGE_API_URL", "localhost")

    return f"{url}:{port}/api/"


async def clear_prices():
    return requests.delete(url=f"{STORAGE_API_URL}/prices")


async def create_prices(symbol_id, data):
    return requests.post(url=f"{STORAGE_API_URL}/prices/{symbol_id}", json=data)


async def get_all_latest_prices():
    return requests.get(url=f"{STORAGE_API_URL}/prices")


async def get_price_from_symbol(symbol_id):
    return requests.get(url=f"{STORAGE_API_URL}/prices/{symbol_id}")


STORAGE_API_URL = __get_storage_api_url()
