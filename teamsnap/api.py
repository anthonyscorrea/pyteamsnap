__all__ = ['TeamSnap', 'Team', 'Event', 'Availability']

from apiclient import APIClient, HeaderAuthentication, JsonResponseHandler
from collection_json import Collection
import json

class ApiObject():
    rel = None

    def __init__(self, client, rel=rel, data={}):
        self.client = client
        self.data = data
        self.rel = rel

    @classmethod
    def search(cls, client, **kwargs):
        results = client.query(cls.rel, "search", **kwargs)
        return [cls(client,rel=cls.rel, data=r) for r in results]

    @classmethod
    def get(cls, client, id):
        r = client.get(f"{client.link(cls.rel)}/{id}")
        return cls(client, cls.rel, client.parse_response(r)[0])

class Me (ApiObject):
    rel = "me"

    def __init__(self, client):
        super().__init__(client=client, rel=self.rel, data=client.get(client.link(self.rel)))

class Event (ApiObject):
    rel = "events"

class Team (ApiObject):
    rel = "teams"
    pass

class Availability (ApiObject):
    rel = "availabilities"
    pass

class TeamSnap(APIClient):
    base_url = 'https://api.teamsnap.com/v3'

    def __init__(self, token, *args, **kwargs):
        super().__init__(*args,
                         authentication_method=HeaderAuthentication(token=token),
                         response_handler=JsonResponseHandler,
                         **kwargs)
        self._root_collection = self.get(self.base_url)['collection']
        self._links = self._by_rel(self.base_url, 'links')
        self._queries = self._by_rel(self.base_url, 'queries')
        self._commands = self._by_rel(self.base_url, 'commands')
        pass

    def link(self, link_name):
        d = {l['rel']:l['href'] for l in self._root_collection["links"]}
        return d.get(link_name)

    def _by_rel (self, url, k):
        try:
            {l['rel']: l for l in self._root_collection[k]}
        except Exception as e:
            return {}
        self.get(url)['collection'][k]
        return {l['rel']:l for l in self.get(url)['collection'][k]}

    def query (self, rel, query, **kwargs):
        queries = self._by_rel(self._get_href(rel), 'queries')
        response = self.get(self._get_href(query, queries), params=kwargs)
        return self.parse_response(response)

    def command (self, rel, command, **kwargs):
        commands = self._by_rel(self._get_href(rel), 'commands')
        response = self.get(self._get_href(command, commands), params=kwargs)
        return self.parse_response(response)

    def _get_href (self, rel: str, links:dict = None, url = base_url) -> str:
        """returns a hyperlink from a the links dictionary. Each item in the links dictionary is a
         dictionary with a rel and href key"""
        if links is None: links = self._by_rel(url, 'links')
        link = links[rel]['href']
        return link

    def get_item (self, rel, id):
        r = self.get(f"{self.link(rel)}/{id}")
        return self.parse_response(r)[0]

    def get_collection(self, rel, id=None):
        if id:
            url = f"{self.link(rel)}/{id}"
        else:
            url = f"{self.link(rel)}"
        r = self.get(url)
        return Collection.from_json(json.dumps(r))

    @classmethod
    def parse_response(self, response):
        result = []
        items = [item['data'] for item in response['collection'].get('items',[])]
        for item in response['collection'].get('items',[]):
            details = {}
            for detail in item['data']:
                # TODO type casting and validation based on item['type']
                details[detail['name']] = detail['value']
            result.append(details)

        return result
        # return [{detail['name']: detail['value'] for detail in item} for item in items]

