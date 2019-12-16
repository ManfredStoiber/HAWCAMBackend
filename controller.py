from flask import Flask, send_from_directory, request, jsonify
import uc_create_category, uc_list_categories

app = Flask(__name__, static_url_path='')

data = {
    "categories": [
        {
            "name": "Raum",
            "count": 3
        },
        {
            "name": "Buch",
            "count": 14
        },
        {
            "name": "Rechner",
            "count": 10
        }
    ]
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
    #result = uc_list_categories.list_categories()
    #return result


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
