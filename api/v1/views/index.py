from views import app_views
from flask import jsonify


@app_views.route("/index", methods=['GET'], strict_slashes=False)
def index():
    return jsonify({"index": "Welcome on BES"})
