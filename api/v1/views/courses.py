from api.v1.views import app_views
from flask import jsonify, make_response, abort

courses = [{"id": "1", "name": "Bitcoin Dev"}]

@app_views.route("/courses", methods=['GET'], strict_slashes=False)
def get_courses():
    return jsonify(courses)

@app_views.route("/courses/<course_id>", methods=['GET'], strict_slashes=False)
def get_course(course_id):
    course = [crs for crs in courses if crs['id'] == course_id]
    if len(course):
        return jsonify(course)
    else:
        abort(404)

@app_views.route("/courses/<course_id>", methods=['DELETE'], strict_slashes=False)
def delete_course(course_id):
    course = [crs for crs in courses if crs['id'] == course_id]
    if len(course):
        courses.remove(course[0])
        return make_response(jsonify({}), 200)
    else:
        abort(404)

@app_views.route("/courses", methods=['POST'], strict_slashes=False)
def add_course():
    try:
        body = {"name": "LN DEV"}
        if "name" in body.keys():
            course = {"id": "4", "name": body["name"]}
            courses.append(course)
            return make_response(jsonify(course), 201)
        else:
            abort(400, description="Missing name")
    except:
        abort(400, description="Not a JSON")
