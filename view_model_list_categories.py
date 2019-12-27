import json
from model_category import Category


class ViewModelListCategories:

    def __init__(self, result_set):
        self.result_set = result_set

    def create_json(self):
        categories_as_dict = []
        for x in self.result_set:
            category_as_dict = {
                "name": x[0],
                "count": x[1]
            }
            categories_as_dict.append(category_as_dict)
        categories_as_dict = sorted(categories_as_dict, key=lambda x: x["name"])
        return json.dumps({"categories": categories_as_dict})


