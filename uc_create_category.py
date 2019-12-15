import json
from model_category import *
from view_model_create_category import ViewModelCreateCategory
from repository import Repository


def create_category(content):
    string = json.dumps(content)
    string_as_dict = json.loads(string)
    # for x, y in string_as_dict.items():
    #	print(x, y)
    view = ViewModelCreateCategory(string_as_dict)
    repository = Repository(view.to_model(), "createCategory")
    if repository is not None:
        check = repository.connect_with_db()
    else:
        check = False
    return check
