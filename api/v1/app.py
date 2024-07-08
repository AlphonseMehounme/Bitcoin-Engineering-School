from views import app_views
from flask import Flask, make_response, jsonify, render_template, request
from os import getenv
import json

app = Flask(__name__)
"""app.register_blueprint(app_views)"""

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/index')
def index():
    return jsonify({"index": "Welcome on BES"})

@app.route('/login')
def login_page() -> 'str':
    return render_template('login.html', the_title='Please log on on BES')

@app.route('/login_result', methods=['POST'])
def login_result_page() -> 'str':

    json_file = "/home/yam1st/BES/Bitcoin-Engineering-School/file.json"
    email = request.form['mail']
    password = request.form['password']

    with open(json_file) as file:
        data = json.load(file)


    courses = []
    for user_id, user_data in data.items():
        if 'email' in user_data and user_data['email'] == email:
            if 'courses' in user_data:
                courses = user_data['courses']

    categories = []
    for user_id, user_data in data.items():
        if 'email' in user_data and user_data['email'] == email:
            if 'categories' in user_data:
                categories = user_data['categories']

    for user, user_data in data.items():
        if 'email' in user_data and 'password' in user_data:
            if user_data['email'] == email and user_data['password'] == password:
                return render_template('login_result.html', the_title='Welcome on BES', the_mail=email, the_password=password)

    return render_template('login_result.html', the_title='Welcome on BES', the_courses=courses, the_categories=categories )

@app.teardown_appcontext
def close_app(exception):
    print("Closing")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "empty, like shitcoins"}), 404)

if __name__ == "__main__":
    HOST = getenv('BES_API_HOST', '127.0.0.1')
    PORT = getenv('BES_API_PORT', 5000)
    app.run(host=HOST, port=PORT, debug=True, threaded=True)
