from views import app_views
from flask import Flask, make_response, jsonify, render_template
from os import getenv

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
    return render_template('login_result.html', the_title='Welcome on BES')

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
