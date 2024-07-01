"""
Category Module
"""
from flask import abort, request, make_response, jsonify
from models.category import Category
from api.v1.views import app_views
from models import storage


@app_views.route("/categories", methods=['GET'], strict_slashes=False)
def get_categories():
    """
    Method to get categories
    """
    categories_objs = storage.all(Category)
    categories = {}
    for key, value in categories_objs.items():
        categories.update({key: value.to_dict()})
    return jsonify(categories)

@app_views.route("/categories/<category_id>", methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """
    Method to get a Category
    """
    category = storage.get(Category, category_id)
    if category:
        return jsonify(category.to_dict())
    else:
        abort(404)

@app_views.route("/categories/<category_id>", methods=['DELETE'], strict_slashes=False)
def delete_category(category_id):
    """
    Method to delete a category
    """
    category = storage.get(Category, category_id)
    if category:
        storage.delete(category)
        return make_response(jsonify({}), 200)
    else:
        abort(404)

@app_views.route("/categories", methods=['POST'], strict_slashes=False)
def add_category():
    """
    Method to add category
    """
    try:
        body = request.get_json()
        if "name" in body.keys():
            category = Category()
            for key, value in body.items():
                category.__dict__[key] = value
            category.save()
            return make_response(jsonify(category.to_dict()), 201)
        else:
            abort(400, "Missing name")
    except:
        abort(400, description="Not a JSON")

@app_views.route("/categories/<category_id>", methods=['PUT'], strict_slashes=False)
def update_category(category_id):
    """
    Method to update a category
    """
    category = storage.get(Category, category_id)
    if category:
        body = request.get_json()
        for key, value in body.items():
            if key not in ["id", "created_at", "updated_at"]:
                category.__dict__[key] = value
        category.save()
        return make_response(jsonify(category.to_dict()), 200)
    else:
        abort(404)
