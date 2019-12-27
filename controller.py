from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import uc_create_category, uc_list_categories, traceback

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route('/api/v1.0/createCategory', methods=['PUT'])
def call_uc_create_category():
    content = request.get_json(force=True)
    try:
        check = uc_create_category.create_category(content)
        print("call_uc_create_category()")
        return content
    except Exception as error:
        print(traceback.format_exc())
        return str(traceback.format_exc())


@app.route("/api/v1.0/listCategories", methods=["GET"])
def call_uc_list_categories():
    # return jsonify(data)
    try:
        result = uc_list_categories.list_categories()
        return result
    except Exception as error:
        return str(error)


if __name__ == '__main__':
    #app.run(port=5000)
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
