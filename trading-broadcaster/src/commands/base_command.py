from abc import ABC, abstractmethod
from typing import Dict, Optional


class BaseCommand(ABC):
    _data_received: Dict
    _path: str
    _ws: any

    def __init__(self, data_received: Dict, path: Optional[str] = "", ws: Optional[any] = None):
        self._data_received = data_received
        self._path = path
        self._ws = ws

    @abstractmethod
    async def process_data_received(self) -> Dict:
        pass
