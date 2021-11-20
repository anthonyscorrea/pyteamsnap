from dataclasses import dataclass
from typing import Optional
from teamsnap.api import TeamSnap
from urllib.parse import urljoin

class Item:
    id: int
    type: str
    data: dict = {}

    def __init__(self, client:TeamSnap, rel, id, data: dict = {}):
        self._client = client
        self.type = rel
        self.id = id
        self._data = data

    @property
    def data(self):
        if self._data: return self._data
        else:
            return self._client.get_item(self.type, self.id)
