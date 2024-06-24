from typing import List

from src.providers.provider import Provider


class ProvidersController:
    _instance = None
    _providers = List[Provider]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProvidersController, cls).__new__(cls)
            cls._instance._providers = []
        return cls._instance

    async def add_provider(self, url: str, symbol: list):
        if not any(a.url == url for a in self._providers):
            provider = Provider(url, symbol)
            self._providers.append(provider)
            await provider.start_listening_provider()

    def clear_providers(self):
        self._providers = []

    def get_providers(self) -> List[Provider]:
        return self._providers


providers = ProvidersController()
