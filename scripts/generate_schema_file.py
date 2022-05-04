from apiclient import HeaderAuthentication
from apiclient import JsonResponseHandler
from tests.credentials import token
from tests.private_test import TeamSnap
import yaml

schema = {}

c = TeamSnap(authentication_method=HeaderAuthentication(token=token), response_handler=JsonResponseHandler)

def generate_schema(verb='queries'):
    for rel, link in c._links.items():
        for query, details in c._by_rel(link['href'], verb).items():
            if not schema.get(rel):
                schema[rel] = {}
            try:
                d = details['data']
                schema[rel][query] = [{k:v for k,v in data.items() if k not in ['value']} for data in details['data']]
            except:
                continue
            print (f"{query=}")

    with open(f'{verb}.yaml', 'w') as f:
        yaml.dump(schema,f)
        pass

generate_schema('queries')