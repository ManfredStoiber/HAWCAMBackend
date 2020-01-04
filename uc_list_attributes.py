from repository import Repository
from view_model_list_attributes import VmListAttributes
import json


def get_attributes(content):
    r = Repository(model=None, uc="listAttributes")
    content = json.loads(json.dumps(content))
    category = content["catName"]
    result = r.connect_with_db(category)
    vm = VmListAttributes(result)
    return vm.create_json(category)


