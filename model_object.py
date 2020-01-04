class ObjectDetail:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.detail_list = [None] * len(self.__dict__)
        i = 0
        for x, y in self.__dict__.items():
            if type(y) is not list:
                if i < (len(self.__dict__) - 1):
                    self.detail_list[i] = y
                    i = i + 1


class Object:
    def __init__(self, cat_name, name, details):
        self.cat_name = cat_name
        self.name = name
        self.details = ObjectDetail(**details)

    def get_tuple(self):
        return (self.name, "0")