from abc import ABC, abstractmethod
from typing import Dict


class BaseCommand(ABC):
    _data_received: Dict

    def __init__(self, data_received: Dict):
        self._data_received = data_received

    @abstractmethod
    async def process_data_received(self) -> Dict:
        pass
