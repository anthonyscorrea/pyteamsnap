import typing as T

from apiclient import (
    APIClient,
    HeaderAuthentication,
    JsonResponseHandler,
    JsonRequestFormatter,
)
from pyteamsnap.models.base import BaseApiObject
import datetime

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
            response_handler=JsonResponseHandler,
            request_formatter=JsonRequestFormatter,
            **kwargs,
        )
        self._root_collection = self.get(self.base_url)["collection"]
        self._links = self._by_rel(self.base_url, "links")
        self._queries = self._by_rel(self.base_url, "queries")
        self._commands = self._by_rel(self.base_url, "commands")
        pass

    def link(self, link_name):
        d = {link["rel"]: link["href"] for link in self._root_collection["links"]}
        return d.get(link_name)

    def bulk_load(
        self, team_id, types: T.List[BaseApiObject], **kwargs
    ) -> T.List[TTeamSnap]:
        """

        :param team_id:
        :param types: List of items to fetch, in the form of BaseApiObject classes
        :param kwargs: Additional filters passed into requested types by passing them in the url's querystring
            as type__filter=value (i.e. ?event__start_date=2015-01-01).
            Any filter can be passed that is available on the search for the specified type.
        :return: Heterogeneous collection of the specified types for a specified team or teams.
        """
        types_dict = {t.type: t for t in types}
        r = self.query(
            rel="self",
            query="bulk_load",
            types=",".join(types_dict.keys()),
            team_id=team_id,
            **kwargs,
        )

        result = []
        for item in r:
            cls = types_dict[item["type"]]
            instance = cls(self, data=item)
            result.append(instance)
        return result

    def _by_rel(self, url: str, record_key: str) -> dict:
        """Get a mapping of record_key to its collection.

        :param url:
        :param record_key: one of "href", "version", "links", "items", "queries", "commands", "template", "error"
        :return: A mapping of record_key to its collection
        """
        collection = self.get(url)["collection"]
        return {collection["rel"]: collection for collection in collection[record_key]}

    def query(self, rel, query: str, **kwargs) -> list:
        queries = self._by_rel(self._get_href(rel), "queries")
        response = self.get(self._get_href(rel=query, links=queries), params=kwargs)
        return self.parse_response(response)

    def command(self, rel, command: str, **kwargs) -> list:
        commands = self._by_rel(self._get_href(rel), "commands")
        response = self.get(self._get_href(command, commands), params=kwargs)
        return self.parse_response(response)

    def _get_href(self, rel: str, links: dict = None, url: str = base_url) -> str:
        """

        :param rel:
        :param links:
        :param url:
        :return: A hyperlink from the links dictionary. Each item in the links dictionary is a
         dictionary with a rel and href key
        """
        try:
            if links is None:
                links = self._by_rel(url, "links")

            link = links[rel]["href"]
        except Exception as e:
            raise e
        return link

    def get_item(self, rel: str, id: T.Union[int, str]) -> dict:
        r = self.get(f"{self.link(rel)}/{id}")
        return self.parse_response(r)[0]

    def post_item(self, rel: str, data: dict) -> dict:
        r = super(TeamSnap, self).post(f"{self.link(rel)}", data=data)
        return self.parse_response(r)[0]

    def put_item(self, rel, id: T.Union[int, str], data: dict) -> dict:
        r = super(TeamSnap, self).put(f"{self.link(rel)}/{id}", data=data)
        return self.parse_response(r)[0]

    def delete_item(self, rel, id: T.Union[int, str]) -> None:
        super(TeamSnap, self).delete(f"{self.link(rel)}/{id}")
        return None

    @classmethod
    def parse_response(self, response: dict) -> list:
        result = []
        for item in response["collection"].get("items", []):
            details = {}
            for detail in item["data"]:
                value = detail["value"]
                value_type = detail["type"]
                if value:
                    if value_type == "DateTime":
                        value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
                    elif value_type == "Boolean":
                        if value is not True:
                            value = False
                    elif value_type == "Integer":
                        value = int(value)
                details[detail["name"]] = value
            result.append(details)

        return result
        # return [{detail['name']: detail['value'] for detail in item} for item in items]
