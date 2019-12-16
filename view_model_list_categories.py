import json
from model_category import Category


class ViewModelListCategories:

    def __init__(self, result_set):
        self.result_set = result_set

    def to_model(self, row):
        return Category(row[0], details=None, deleted=None)

    def create_json(self):
        categories_as_dict = []
        for x in self.result_set:
            category = self.to_model(x)
            print("cat-name = " + str(category.name))
            print("count = " + str(x[1]))
            category_as_dict = {
                "name": category.name,
                "count": x[1]
            }
            categories_as_dict.append(category_as_dict)
        return json.dumps({"categories": categories_as_dict})


