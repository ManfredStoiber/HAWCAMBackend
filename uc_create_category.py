import json
from model_category import *
from view_model_create_category import ViewModelCreateCategory
from repository import Repository


def create_category(content):
    string = json.dumps(content)
    string_as_dict = json.loads(string)
    view = ViewModelCreateCategory(string_as_dict)
    repository = Repository(view.to_model(), "createCategory")
    repository.connect_with_db()
