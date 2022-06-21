from apiclient import APIClient, HeaderAuthentication, JsonResponseHandler, JsonRequestFormatter
import datetime

class TeamSnap(APIClient):
    base_url = 'https://api.teamsnap.com/v3'

    def __init__(self, token, *args, **kwargs):
        super().__init__(*args,
                         authentication_method=HeaderAuthentication(token=token),
                         response_handler=JsonResponseHandler,
                         request_formatter=JsonRequestFormatter,
                         **kwargs)
        self._root_collection = self.get(self.base_url)['collection']
        self._links = self._by_rel(self.base_url, 'links')
        self._queries = self._by_rel(self.base_url, 'queries')
        self._commands = self._by_rel(self.base_url, 'commands')
        pass

    def link(self, link_name):
        d = {l['rel']:l['href'] for l in self._root_collection["links"]}
        return d.get(link_name)

    def bulk_load(self, team_id, types, **kwargs):
        """
        Returns a heterogeneous collection of the specified types for a specified team or teams.
        Additional filters can be passed into requested types by passing them in the url's querystring
        as type__filter=value (i.e. ?event__start_date=2015-01-01).
        Any filter can be passed that is available on the search for the specified type.
        :param team_id:
        :param types:
        :param kwargs:
        :return:
        """
        types_dict = {t.type:t for t in types}
        r = self.query(
            rel="self",
            query="bulk_load",
            types=",".join(types_dict.keys()),
            team_id=team_id,
            **kwargs
        )

        result = []
        for item in r:
            cls = types_dict[item['type']]
            instance = cls(self, rel=cls.rel, data=item)
            result.append(instance)
        return result

    def _by_rel (self, url, k):
        # try:
        #     return {l['rel']: l for l in self._root_collection[k]}
        # except Exception as e:
        #     return {}
        # self.get(url)['collection'][k]
        return {l['rel']:l for l in self.get(url)['collection'][k]}

    def query (self, rel, query, **kwargs):
        queries = self._by_rel(self._get_href(rel), 'queries')
        response = self.get(self._get_href(rel=query, links=queries), params=kwargs)
        return self.parse_response(response)

    def command (self, rel, command, **kwargs):
        commands = self._by_rel(self._get_href(rel), 'commands')
        response = self.get(self._get_href(command, commands), params=kwargs)
        return self.parse_response(response)

    def _get_href (self, rel: str, links:dict = None, url = base_url) -> str:
        """returns a hyperlink from a the links dictionary. Each item in the links dictionary is a
         dictionary with a rel and href key"""
        try:
            if links is None: links = self._by_rel(url, 'links')

            link = links[rel]['href']
        except Exception as e:
            pass
        return link

    def get_item (self, rel, id):
        r = self.get(f"{self.link(rel)}/{id}")
        return self.parse_response(r)[0]

    def post_item(self, rel, data):
        r = super(TeamSnap, self).post(f"{self.link(rel)}", data=data)
        return self.parse_response(r)[0]

    def put_item(self, rel, id, data):
        r = super(TeamSnap, self).put(f"{self.link(rel)}/{id}", data=data)
        return self.parse_response(r)[0]

    def delete_item(self, rel, id):
        r = super(TeamSnap, self).delete(f"{self.link(rel)}/{id}")
        return None

    @classmethod
    def parse_response(self, response):
        result = []
        items = [item['data'] for item in response['collection'].get('items',[])]
        for item in response['collection'].get('items',[]):
            details = {}
            for detail in item['data']:
                value = detail['value']
                value_type = detail['type']
                if value:
                    if value_type == 'DateTime':
                        value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z')
                    elif value_type == 'Boolean':
                        value = value == True
                    elif value_type == 'Integer':
                        value = int(value)
                details[detail['name']] = value
            result.append(details)

        return result
        # return [{detail['name']: detail['value'] for detail in item} for item in items]
