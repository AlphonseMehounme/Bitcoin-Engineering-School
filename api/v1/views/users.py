"""
Users Module
"""
from flask import jsonify, abort, make_response, request
from models.user import User
from models import storage
from api.v1.views import app_views


@app_views("/users", methods=['GET'], strict_slashes=False)
def get_user():
    """
    Method to get a user
    """
    users_json = storage.all(User)
    users = {}
    for key, value in users_json.items():
        users.update({key: value.to_dict()})
    return jsonify(users)
