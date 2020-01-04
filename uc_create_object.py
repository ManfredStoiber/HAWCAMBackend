import json
from model_category import *
from view_model_create_object import ViewModelCreateObject
from repository import Repository


def create_object(content):
    string = json.dumps(content)
    string_as_dict = json.loads(string)
    view = ViewModelCreateObject(string_as_dict)
    repository = Repository(view.to_model(), "createObject")
    repository.connect_with_db()
