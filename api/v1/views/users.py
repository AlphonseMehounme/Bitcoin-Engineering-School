"""
Users Module
"""
from flask import jsonify, abort, make_response, request
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views.route("/users", methods=['GET'], strict_slashes=False)
def get_users():
    """
    Method to get a user
    """
    users_json = storage.all(User)
    users = {}
    for key, value in users_json.items():
        users.update({key: value.to_dict()})
    return jsonify(users)

@app_views.route("/users/<user_id>", methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Method to get a user
    """
    user_obj = storage.get(User, user_id)
    if user_obj:
        return jsonify(user_obj.to_dict())
    else:
        abort(404)
