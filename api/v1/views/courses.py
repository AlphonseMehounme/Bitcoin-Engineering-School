"""
Course Module
"""
from api.v1.views import app_views
from flask import jsonify, make_response, abort, request
from models import storage
from models.course import Course


@app_views.route("/categories/<category_id>/courses")
def get_category_courses(category_id):
    """
    Get courses for a category
    """
    courses_ojbs = storage.get(Course)
    return jsonify({})

@app_views.route("/courses", methods=['GET'], strict_slashes=False)
def get_courses():
    """
    Return all courses
    """
    courses_objs = storage.all(Course)
    courses = {}
    for key, value in courses_objs.items():
        courses.update({key: value.to_dict()})
    return jsonify(courses)

@app_views.route("/courses/<course_id>", methods=['GET'], strict_slashes=False)
def get_course(course_id):
    """
    Return a specific course based on course_id
    """
    course = storage.get(Course, course_id)
    print(course)
    if course:
        return jsonify(course.to_dict())
    else:
        abort(404)

@app_views.route("/courses/<course_id>", methods=['DELETE'], strict_slashes=False)
def delete_course(course_id):
    """
    Delete a specific course based on course_id
    """
    course = storage.get(Course, course_id)
    if course:
        storage.delete(course)
        return make_response(jsonify({}), 200)
    else:
        abort(404)

@app_views.route("/courses", methods=['POST'], strict_slashes=False)
def add_course():
    """
    Add new course
    """
    try:
        body = request.get_json()
        print(body)
        if "name" in body.keys():
            course = Course()
            for key, value in body.items():
                if key not in ["id", "created_at", "updated_at"]:
                    course.__dict__[key] = value
            course.save()
            return make_response(jsonify(course.to_dict()), 201)
        else:
            abort(400, description="Missing name")
    except:
        abort(400, description="Not a JSON")

@app_views.route("/courses/<course_id>", methods=['PUT'], strict_slashes=False)
def update_course(course_id):
    """
    Update a specific course based on course_id
    """
    course = storage.get(Course, course_id)
    if course:
        try:
            body = request.get_json()
            for key, value in body.items():
                if key not in ['id', 'created_at', 'updated_at']:
                    course.__dict__[key] = value
            course.save()
            return make_response(jsonify(course.to_dict()), 200)
        except:
            abort(400, description="Not a JSON")
    else:
        abort(404)
