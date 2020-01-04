from model_category import *


class ViewModelCreateCategory:

    def __init__(self, string_as_dict):
        self.dict = string_as_dict

    def to_model(self):
        category = Category(self.dict["name"], self.dict["contentDescriptions"], self.dict["deleted"])
        return category
