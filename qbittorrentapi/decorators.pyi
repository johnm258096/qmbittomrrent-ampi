from typing import Callable
from typing import Set
from typing import Text
from typing import Type

from qbittorrentapi.client import Client
from qbittorrentapi.definitions import Dictionary
from qbittorrentapi.definitions import List
from qbittorrentapi.request import Request

class Alias:
    aliases: Set[Text]
    def __init__(self, *aliases: Text) -> None: ...
    def __call__(self, f: Callable) -> Callable: ...

def aliased(aliased_class: Type[Request]): ...
def login_required(func: Callable): ...
def handle_hashes(func: Callable): ...
def response_text(response_class: Type[int | Text]): ...
def response_json(response_class: Type[List | Dictionary]): ...
def _check_for_raise(client: Client, error_message: Text) -> None: ...
def _version_too_old(client: Client, version_to_compare: Text) -> bool: ...
def _version_too_new(client: Client, version_to_compare: Text) -> bool: ...
def endpoint_introduced(version_introduced: Text, endpoint: Text): ...
def version_removed(version_obsoleted: Text, endpoint: Text): ...
