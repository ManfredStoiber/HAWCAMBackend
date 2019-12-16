from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS, cross_origin
#from flask_restful import Resource, Api
import uc_create_category

app = Flask(__name__, static_url_path='')
CORS(app)

data = {
    "categories": {
        "1": {
            "name": "Raum",
            "count": 3
        },
        "2": {
            "name": "Buch",
            "count": 14
        },
        "3": {
            "name": "Rechner",
            "count": 10
        }
    }
}


@app.route('/api/v1.0/createCategory', methods=['PUT'])
def call_uc_create_category():
    content = request.get_json(force=True)
    uc_create_category.create_category(content)
    print("Content = " + str(content))
    return content


@app.route("/api/v1.0/listCategories", methods=["GET"])
def call_uc_list_categories():
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=5000)
