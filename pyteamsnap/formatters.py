from apiclient.response_handlers import BaseResponseHandler
from apiclient.request_formatters import BaseRequestFormatter
from apiclient.response import Response
from typing import Optional
from apiclient.exceptions import ResponseParseError
from apiclient.utils.typing import JsonType, XmlType, OptionalJsonType, OptionalStr
from json import JSONDecodeError
from collection_json import Collection
import json
import datetime

def date_hook(obj):
    t = type(obj)

    if t is dict:
        return {k: date_hook(v) for k, v in obj.items()}
    if t is list:
        return [date_hook(elem) for elem in obj]
    if t is str:
        if "-" in obj and "Z" in obj and "Z" in obj and len(obj) == 20:
            try:
                return datetime.datetime.strptime(obj, "%Y-%m-%dT%H:%M:%S%z")
            except ValueError as e:
                raise e
        elif obj.count('-') == 2 and len(obj) == 10:
            try:
                return datetime.datetime.strptime(obj, "%Y-%m-%d")
            except ValueError as e:
                raise e
        return obj
    return obj

class CollectionJsonResponseHandler(BaseResponseHandler):
    """Attempt to return the decoded response data as json."""

    @staticmethod
    def get_request_data(response: Response) -> Optional[JsonType]:
        if response.get_raw_data() == "":
            return None

        try:
            response_json_collection = Collection.from_json(response.get_raw_data(), object_hook=date_hook)
        except JSONDecodeError as error:
            raise ResponseParseError(
                f"Unable to decode response data to json. data='{response.get_raw_data()}'"
            ) from error
        return response_json_collection

class CollectionJsonRequestFormatter(BaseRequestFormatter):
    """Format the outgoing data as json."""

    content_type = "application/json"

    @classmethod
    def format(cls, data: OptionalJsonType) -> OptionalStr:
        if data:
            return json.dumps(data)
