from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import uc_create_category
import uc_list_categories
import uc_list_attributes
import uc_create_object

app = Flask(__name__, static_url_path='')
CORS(app)

data_object_details = {
    "name": "R123",
    "details":
        [
            {"name": "Bezeichung", "typ": "textfield", "mandatory": "1", "value": "R123"},
            {"name": "Sitzform", "typ": "textfield", "mandatory": "0", "value": "U-Form"},
            {"name": "Anzahl", "typ": "number", "mandatory": "1", "value": 34}
        ]
}

data_search = {
    "categories":
        [
            {"name": "Raum"},
            {"name": "Raumtisch"},
            {"name": "Raumwand"}
        ],
    "objects":
        [
            {"name": "Raum1", "cat": "Raum"},
            {"name": "Raum2", "cat": "Raum"},
            {"name": "Raumtisch2", "cat": "Raumtisch"}
        ]
}

data_search_failed = {
    "categories":
        [
        ],
    "objects":
        [
        ]
}

data_search_one_object = {
    "categories":
        [
        ],
    "objects":
        [
            {"name": "R232", "cat": "Raum"}
        ]
}


def create_error_json(content):
    return {"Fehler": content}


@app.route('/api/v1.0/createCategory', methods=['PUT'])
def call_uc_create_category():
    try:
        content = request.get_json(force=True)
        uc_create_category.create_category(content)
        return content
    except Exception as error:
        return create_error_json(str(error))


@app.route("/api/v1.0/listCategories", methods=["GET"])
def call_uc_list_categories():
    # return jsonify(data)
    try:
        result = uc_list_categories.list_categories()
        return result
    except Exception as error:
        return create_error_json(str(error))


@app.route("/api/v1.0/listAttributesForCategory", methods=["PUT"])  # put mit jeweiligem Kategoriename
def call_uc_list_attributes():
    try:
        content = request.get_json(force=True)
        result = uc_list_attributes.get_attributes(content)
        return result
    except Exception as error:
        return create_error_json(str(error))


@app.route("/api/v1.0/createObject", methods=["PUT"])
def call_uc_create_object():
    try:
        content = request.get_json(force=True)
        uc_create_object.create_object(content)
        return content
    except Exception as error:
        return create_error_json(str(error))


# dummy-Service
@app.route("/api/v1.0/editCategory", methods=["PUT"])
def call_uc_edit_category():
    try:
        content = request.get_json(force=True)
        return content
    except Exception as error:
        return create_error_json(str(error))


# dummy-Service
@app.route("/api/v1.0/editObject", methods=["PUT"])
def call_uc_edit_object():
    try:
        content = request.get_json(force=True)
        return content
    except Exception as error:
        return create_error_json(str(error))


# dummy-Service
@app.route("/api/v1.0/listObjectDetails", methods=["PUT"])
def call_uc_list_object_details():
    try:
        content = request.get_json(force=True)
        return jsonify(data_object_details)
    except Exception as error:
        return create_error_json(str(error))


# dummy-Service
@app.route("/api/v1.0/search", methods=["PUT"])
def call_uc_search():
    try:
        content = request.get_json(force=True)
        return jsonify(data_search)
    except Exception as error:
        return create_error_json(str(error))


# dummy-Service
@app.route("/api/v1.0/searchFailed", methods=["PUT"])
def call_uc_search_failed():
    try:
        content = request.get_json(force=True)
        return jsonify(data_search_failed)
    except Exception as error:
        return create_error_json(str(error))


# dummy-Service
@app.route("/api/v1.0/searchOneObject", methods=["PUT"])
def call_uc_search_one_object():
    try:
        content = request.get_json(force=True)
        return jsonify(data_search_one_object)
    except Exception as error:
        return create_error_json(str(error))


if __name__ == '__main__':
    # app.run(port=5000)
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
