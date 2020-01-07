import json
from view_model_search import ViewModelSearch
from repository import Repository


def list_categories():
    repository = Repository(model=None, uc="search")
    result = repository.connect_with_db()
    vm = ViewModelSearch(result)
    json_object = vm.create_json()
    return json_object