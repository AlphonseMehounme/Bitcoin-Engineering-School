from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_app(exception):
    print("Closing")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "empty, like shitcoins"}), 404)

if __name__ == "__main__":
    HOST = getenv('BES_API_HOST', '0.0.0.0')
    PORT = getenv('BES_API_PORT', 5000)
    app.run(host=HOST, port=PORT, threaded=True)
