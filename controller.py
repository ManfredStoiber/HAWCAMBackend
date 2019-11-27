from flask import Flask, send_from_directory, request
import uc_create_category

app = Flask(__name__, static_url_path='')

@app.route('/api/v1.0/createCategory', methods=['GET', 'POST'])
def call_uc_create_category():
    content = request.get_json(force=True)
    uc_create_category.create_category(content)
    return content

if __name__ == '__main__':
    app.run(port=5000)
