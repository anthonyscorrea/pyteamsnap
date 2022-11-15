from __future__ import annotations
import apiclient.exceptions
from apiclient import (
    APIClient,
)
import typing as T
from abc import ABC
from itertools import chain


# Import "preview" of Self typing
# https://stackoverflow.com/a/70932112
from typing_extensions import Self

class NotPossibleError(Exception):
    """Raised for actions that are not possible to perform this action per API"""
    pass

class BaseApiObject(ABC):
    rel: str = None
    version: str = None

    __slots__ = [
        'client',
        'id',
        'id_',
    ]

    def __init__(
        self, client: APIClient, data: T.Dict[str, T.Union[str, list]] = {}
    ) -> None:
        """

        :param client:
        :param data: Data to instantiate instance, defaults to empty dict.
        """
        self.client = client

        slots = list(chain.from_iterable(getattr(cls, '__slots__', []) for cls in self.__class__.__mro__))
        for k, v in data.items():
            if k == "id" :
                setattr(self, 'id', v) #TODO remove this, here for backward compatibility, but bad idea
                setattr(self, 'id_', v)
            elif k in ['type', 'rel']: #read only, inherit to class type
                continue
            elif k in slots:
                setattr(self, k, v)
            else:
                # print(f'Warning: {k} not in {self}')
                pass
        pass


    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<TeamSnap {self.__class__.__name__} id={self.id_} name="{self.rel}">'


    @property
    def data(self) -> T.Dict[str, T.Union[str, list]]:
        """Data dictionary for object

        :return: dict: dict with keys:
        """
        slots = chain.from_iterable(getattr(cls, '__slots__', []) for cls in self.__class__.__mro__)
        return {k:getattr(self, k, None) for k in slots}

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
        return cls(client, client.parse_response(r)[0])

    @classmethod
    def new(cls, client: Self) -> Self:
        return cls(client)

    def post(self) -> Self:
        data = {
            "template": {
                "data": [{"name": k, "value": v} for k, v in self.data.items()]
            }
        }
        r = self.client.post_item(self.rel, data=data)
        return self

    def put(self) -> Self:
        data = {
            "template": {
                "data": [{"name": k, "value": str(v)} for k, v in self.data.items()]
            }
        }
        id = self.data.get("id")
        r = self.client.put_item(self.rel, id=id, data=data)
        return self

    def delete(self):
        self.client.delete_item(self.rel, id=self.data["id"])
