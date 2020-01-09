import json
from view_model_search import ViewModelSearch
from repository import Repository


def search(content):
    repository = Repository(model=None, uc="search")
    search_pattern = content["search"]
    result = repository.connect_with_db(search_pattern)
    vm = ViewModelSearch(result)
    json_object = vm.create_json()
    return json_object