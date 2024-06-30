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
    users_objs = storage.all(User)
    users = {}
    for key, value in users_objs.items():
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

@app_views.route("/users/<user_id>", methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    Method to delete a user
    """
    user_obj = storage.get(User, user_id)
    if user_obj:
        storage.delete(user_obj)
        return make_response(jsonify({}), 200)
    else:
        abort(404)
