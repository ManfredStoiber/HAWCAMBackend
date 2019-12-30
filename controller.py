from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
import uc_create_category
import uc_list_categories
import uc_list_attributes

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/api/v1.0/createCategory', methods=['PUT'])
def call_uc_create_category():
    content = request.get_json(force=True)
    try:
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
    content = request.get_json(force=True)
    try:
        result = uc_list_attributes.get_attributes(content)
        return result
    except Exception as error:
        return create_error_json(str(error))


# dummy-Service
@app.route("/api/v1.0/createObject", methods=["PUT"])
def call_uc_create_object():
    try:
        content = request.get_json(force=True)
        return content
    except Exception as error:
        return create_error_json(str(error))


if __name__ == '__main__':
    # app.run(port=5000)
    app.debug = True
    app.run(host="0.0.0.0", port=5000)


def create_error_json(content):
    return {"Fehler": content}
