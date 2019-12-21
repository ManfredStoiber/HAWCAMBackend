import json
from view_model_list_categories import ViewModelListCategories
from repository import Repository


def list_categories():
    repository = Repository(model=None, uc="listCategories")
    result = repository.connect_with_db()
    vm = ViewModelListCategories(result)
    json_object = vm.create_json()
    return json_object
