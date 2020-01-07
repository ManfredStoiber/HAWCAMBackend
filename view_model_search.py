import json


class ViewModelSearch:

    def __init__(self, result_set):
        self.result_set = result_set

    def create_json(self, category):
        attributes_as_dict = []
        for x in self.result_set:
            attribute_as_dict = {
                "name": x[0],
                "typ": x[1],
                "mandatory": x[2]
            }
            attributes_as_dict.append(attribute_as_dict)
        attributes_as_dict = sorted(attributes_as_dict, key=lambda y: y["name"])
        print(category[1:-1])
        return json.dumps({"name": category[1:-1], "attributes": attributes_as_dict})
