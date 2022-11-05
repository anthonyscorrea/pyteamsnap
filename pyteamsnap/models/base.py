from __future__ import annotations
import apiclient.exceptions
from apiclient import (
    APIClient,
)
import typing as T

# Import "preview" of Self typing
# https://stackoverflow.com/a/70932112
from typing_extensions import Self


class BaseApiObject:
    rel: str = None
    version: str = None

    def __init__(
        self, client: APIClient, data: T.Dict[str, T.Union[str, list]] = {}
    ) -> None:
        """

        :param client:
        :param data: Data to instantiate instance, defaults to empty dict.
        """
        self.client = client
        self._data = data
        self.rel = self.__class__.rel
        """rel: Relationship between a linked resource and the current document"""

    def __repr__(self):
        return f'TeamSnap<{self.__class__.__name__}:{self.id}> "{self.__str__()}"'

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __setitem__(self, key, newvalue):
        return self._data.__setitem__(key, newvalue)

    def __iter__(self):
        return iter(self._data.items())

    @property
    def id(self) -> int:
        return self._data["id"]

    @property
    def data(self) -> T.Dict[str, T.Union[str, list]]:
        """Data dictionary for object

        :return: dict: dict with keys:
        """
        return self._data

    @classmethod
    def search(cls, client: APIClient, **kwargs):
        try:
            results = client.query(cls.rel, "search", **kwargs)
        except apiclient.exceptions.ServerError as e:
            raise e
        return [cls(client, data=r) for r in results]

    @classmethod
    def get(cls, client: APIClient, id: T.Union[int, str]) -> Self:
        r = client.get(f"{client.link(cls.rel)}/{id}")
        return cls(client, cls.rel, client.parse_response(r)[0])

    @classmethod
    def new(cls, client: Self) -> Self:
        return cls(client, cls.rel)

    def post(self) -> Self:
        data = {
            "template": {
                "data": [{"name": k, "value": v} for k, v in self.data.items()]
            }
        }
        r = self.client.post_item(self.rel, data=data)
        self._data = r
        return self

    def put(self) -> Self:
        data = {
            "template": {
                "data": [{"name": k, "value": str(v)} for k, v in self.data.items()]
            }
        }
        id = self.data.get("id")
        r = self.client.put_item(self.rel, id=id, data=data)
        self._data = r
        return self

    def delete(self):
        self.client.delete_item(self.rel, id=self.data["id"])
