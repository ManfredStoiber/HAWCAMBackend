import json


class VmListAttributes:

    def __init__(self, result_set):
        self.result_set = result_set

    def create_json(self):
        attributes_as_dict = []
        for x in self.result_set:
            attribute_as_dict = {
                "name": x[0],
                "typ": x[1],
                "mandatory": x[2]
            }
            attributes_as_dict.append(attribute_as_dict)
        attributes_as_dict = sorted(attributes_as_dict, key=lambda y: y["name"])
        return json.dumps({"attributes": attributes_as_dict})
