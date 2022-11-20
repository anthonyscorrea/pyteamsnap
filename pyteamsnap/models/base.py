from __future__ import annotations
import apiclient.exceptions
import pyteamsnap.client
import typing as T
from abc import ABC
from itertools import chain
from collection_json import Collection

# Import "preview" of Self typing
# https://stackoverflow.com/a/70932112
from typing_extensions import Self


class NotPossibleError(Exception):
    """Raised for actions that are not possible to perform per API"""
    pass


class BaseTeamsnapObject(ABC):
    rel: str = None
    version: str = None

    __slots__ = [
        'client',
        'id',
        'id_',
    ]

    def __init__(
        self, client: pyteamsnap.client.TeamSnap, data: T.Dict[str, T.Union[str, list]] = {}
    ) -> None:
        """

        :param client: TeamSnap client
        :param data: Data to instantiate instance, defaults to empty dict.
        """
        self.client = client

        slots = list(chain.from_iterable(getattr(cls, '__slots__', []) for cls in self.__class__.__mro__))
        for k, v in data.items():
            if k == "id":
                setattr(self, 'id',
                        v)  # remove id property from BaseTeamsnapObject, here for backward compatibility, but bad idea
                setattr(self, 'id_', v)
            elif k in ['type', 'rel']:  # read only, inherit to class type
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
        return f'<{self.__class__.__name__} id={self.id_}>'

    @property
    def data(self) -> T.Dict[str, T.Union[str, list]]:
        """Data dictionary for object

        :return: dict: dictionary with object's properties
        """
        slots = chain.from_iterable(getattr(cls, '__slots__', []) for cls in self.__class__.__mro__)
        data = {k: getattr(self, k, None) for k in slots}

        data['id'] = data.pop('id_')

        return data

    @classmethod
    def search(cls, client: pyteamsnap.client.TeamSnap, **kwargs) -> T.List[Self]:
        """

        :param client:
        :param kwargs:
        :return: List of TeamSnapBaseObjects
        """
        try:
            results = client.query(cls.rel, "search", **kwargs)
        except apiclient.exceptions.ServerError as e:
            raise e
        return [cls(client, data=result) for result in results]

    @classmethod
    def get(cls, client: pyteamsnap.client.TeamSnap, id_: T.Union[int, str]) -> Self:
        """
        Get one TeamsnapBaseObject from the client
        :param client: T
        :param id_: TeamSnap id of the desired object
        :return:
        """
        result = client.get_item(cls.rel, id_)
        return cls(client, data=result)

    @classmethod
    def new(cls, client: pyteamsnap.client.TeamSnap, data: dict = {}) -> Self:
        """
        Creates a new, blank TeamsnapBaseobject
        :param client: TeamSnap client
        :param data: TeamSnap client
        :return:
        """
        return cls(client, data=data)

    def post(self) -> Self:
        ''' Create object on

        :return:
        '''
        data = [{"name": k, "value": v} for k, v in self.data.items()]
        collection = Collection(template={'data':data})
        response = self.client.post_item(self.rel, data=collection)
        if response:
            return self
        else:
            raise Exception

    def put(self) -> Self:
        data = [{"name": k, "value": v} for k, v in self.data.items()]
        collection = Collection(template={'data': data})
        id = collection.template.id.value
        response = self.client.put_item(self.rel, id=id, data=data)
        if response:
            return self
        else:
            raise Exception

    def delete(self):
        self.client.delete_item(self.rel, id=self.data["id"])
