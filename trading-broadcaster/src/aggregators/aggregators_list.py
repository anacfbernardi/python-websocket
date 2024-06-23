from typing import List

from src.aggregators.aggregator import Aggregator


class AggregatorsList:
    _instance = None
    _aggregators = List[Aggregator]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AggregatorsList, cls).__new__(cls)
            cls._instance._aggregators = []
        return cls._instance

    async def add_aggregator(self, url: str):
        if not any(a.url == url for a in self._aggregators):
            aggregator = Aggregator(url)
            self._aggregators.append(aggregator)
            await aggregator.start_listening_aggregator()

    async def remove_aggregator(self, url):
        aggregator = any(a.url == url for a in self._aggregators)
        if aggregator is not None:
            await aggregator.stop_listening_aggregator()
        self._aggregators = [a for a in self._aggregators if a.url != url]

    def get_aggregators(self) -> List[Aggregator]:
        return self._aggregators

    def get_aggregator_with_min_providers_count(self):
        return min(self._aggregators, key=lambda a: a.providers_count) if len(self._aggregators) else None


aggregators = AggregatorsList()
