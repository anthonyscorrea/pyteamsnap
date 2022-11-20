import typing as T

from apiclient import (
    APIClient,
    HeaderAuthentication,
    JsonResponseHandler,
    JsonRequestFormatter,
)
from pyteamsnap.models.base import BaseTeamsnapObject
import datetime
from pyteamsnap.formatters import CollectionJsonResponseHandler, CollectionJsonRequestFormatter

TTeamSnap = T.TypeVar("TTeamSnap", bound="TeamSnap")


class TeamSnap(APIClient):
    """A client to access the TeamSnap API

    The TeamSnap API is a hypermedia JSON API, using Collection+JSON.
    """

    base_url: str = "https://api.teamsnap.com/v3"

    def __init__(self, token: str, *args, **kwargs) -> None:
        super().__init__(
            *args,
            authentication_method=HeaderAuthentication(token=token),
            response_handler=CollectionJsonResponseHandler,
            request_formatter=CollectionJsonRequestFormatter,
            **kwargs,
        )
        self._root_collection = self.get(self.base_url)
        self._links = self._root_collection.links
        self._queries = self._root_collection.queries
        # self._commands = self._root_collection.commands # TODO add 'commands' in the future. It is non-standard
        pass

    def link(self, link_name):
        d = {link["rel"]: link["href"] for link in self._root_collection["links"]}
        return d.get(link_name)

    def bulk_load(
        self, team_id, types: T.List[BaseTeamsnapObject], **kwargs
    ) -> T.List[TTeamSnap]:
        """

        :param team_id:
        :param types: List of items to fetch, in the form of BaseTeamsnapObject classes
        :param kwargs: Additional filters passed into requested types by passing them in the url's querystring
            as type__filter=value (i.e. ?event__start_date=2015-01-01).
            Any filter can be passed that is available on the search for the specified type.
        :return: Heterogeneous collection of the specified types for a specified team or teams.
        """
        types_dict = {t.type: t for t in types}
        r = self.query(
            rel="root",
            query="bulk_load",
            types=",".join(types_dict.keys()),
            team_id=team_id,
            **kwargs
        )

        result = []
        for item in r:
            cls = types_dict[item['type']]
            instance = cls(self, data=item)
            result.append(instance)
        return result

    def query(self, rel, query: str, **kwargs) -> list:
        if rel == 'root':
            queries = self._root_collection.queries
        else:
            href = self._root_collection.links.get(rel=rel).href
            queries = self.get(href).queries

        response = self.get(
                queries.get(rel=query).href,
                params=kwargs)
        parsed_response = [{d.name: d.value for d in item.data} for item in response.items]
        return parsed_response

    def command(self, rel, command: str, **kwargs) -> list:
        raise NotImplementedError

    def get_item(self, rel: str, id: T.Union[int, str]) -> dict:
        href = self._root_collection.links.get(rel=rel).href
        response = self.get(f"{href}/{id}")
        item = response.items[0]
        return {d.name: d.value for d in item.data}

    def post_item(self, rel: str, data: dict) -> dict:
        r = super(TeamSnap, self).post(f"{self.link(rel)}", data=data)
        return self.parse_response(r)[0]

    def put_item(self, rel, id: T.Union[int, str], data: dict) -> dict:
        r = super(TeamSnap, self).put(f"{self.link(rel)}/{id}", data=data)
        return self.parse_response(r)[0]

    def delete_item(self, rel, id: T.Union[int, str]) -> None:
        super(TeamSnap, self).delete(f"{self.link(rel)}/{id}")
        return None
