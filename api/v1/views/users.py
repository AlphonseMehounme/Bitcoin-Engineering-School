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
    Method to get a user based on user_id
    """
    user_obj = storage.get(User, user_id)
    if user_obj:
        return jsonify(user_obj.to_dict())
    else:
        abort(404)

@app_views.route("/users/<user_id>", methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    Method to delete a user based on user_id
    """
    user_obj = storage.get(User, user_id)
    if user_obj:
        storage.delete(user_obj)
        return make_response(jsonify({}), 200)
    else:
        abort(404)

@app_views.route("/users", methods=['POST'], strict_slashes=False)
def add_user():
    """
    Method to add a new user
    """
    try:
        body = request.get_json()
        if "email" not in body.keys():
            abort(400, description="Missing email")
        elif "password" not in body.keys():
            abort(400, description="Missing password")
        else:
            user = User()
            for key, value in body.items():
                if key not in ["id", "created_at", "updated_at"]:
                    user.__dict__[key] = value
            user.save()
            return make_response(jsonify(user.to_dict()), 201)
    except:
        abort(400, description="Not a JSON")

@app_views.route("/users/<user_id>", methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """
    Method to update a user based on user_id
    """
    user_obj = storage.get(User, user_id)
    if user_obj:
        try:
            body = request.get_json()
            for key, value in body.items():
                if key not in ["id", "email", "created_at", "updated_at"]:
                    user_obj.__dict__[key] = value
            user_obj.save()
            return make_response(jsonify(user_obj.to_dict()), 200)
        except:
            abort(400, description="Not a JSON")
    else:
        abort(404)
