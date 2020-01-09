import json


class ViewModelSearch:

    def __init__(self, result_set):
        self.result_set = result_set    # speichert alle Results der SELECT-Befehle in Repository, aber Kategorie- und Object-Results gemischt

    def create_json(self):
        # if-else prüft, ob SELECTs auf DB überhaupt ein result gebracht haben
        if len(self.result_set) > 0:
            obj_tuple = tuple()
            cat_tuple = tuple()

            # Aufbrechen des Object-Attributs auf die Zeilen von Kategorie-Select und Objekt-Select
            for x in self.result_set:
                if len(x) > 1:
                    obj_tuple = obj_tuple + (x,)
                else:
                    cat_tuple = cat_tuple + (x,)

            # Bau eines Dicts [], in dem die Kategorie-Results als Objekte aneinander gereiht werden: Sieht dann so aus: [{}, {}]
            search_as_dict = []
            for x in cat_tuple:
                if x:                           # prüfen, ob tuple leer oder nicht
                    cat_as_dict = {
                        "name": x[0]
                    }
                    search_as_dict.append(cat_as_dict)
            all_cats_as_dict = sorted(search_as_dict, key=lambda y: y["name"])

            # Bau eines Dicts [] wie oben, nur für Objekt-Results
            search_as_dict = []
            for x in obj_tuple:
                if x:
                    obj_as_dict = {
                        "name": x[0],
                        "cat": x[1]
                    }
                    search_as_dict.append(obj_as_dict)

            # sortieren der Results, damit Reihenfolge nicht variiert und Tests fehlschlagen
            all_objs_as_dict = sorted(search_as_dict, key=lambda y: y["name"])
            return json.dumps({"categories": all_cats_as_dict, "objects": all_objs_as_dict})
        else:
            return json.dumps({"categories": [], "objects": []})

