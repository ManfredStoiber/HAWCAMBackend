from model_object import *


class ViewModelCreateObject:

    def __init__(self, string_as_dict):
        self.dict = string_as_dict

    def to_model(self):
        obj = Object(self.dict["catName"], self.dict["objObjName"], self.dict["details"])
        return obj
