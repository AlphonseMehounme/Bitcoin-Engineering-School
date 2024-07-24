"""
Main Module of our application
"""
from api.v1.views import app_views
from flask import Flask, make_response, jsonify, render_template, request, send_from_directory
from os import getenv
import json

app = Flask(__name__)
app.register_blueprint(app_views)

@app.route('/')
def bes() -> str:
    """
    Handles / route and return Homepage
    """
    return render_template('landing_page.html', the_title='Bitcoin Engineering School')

@app.route('/join')
def index() -> str:
    """
    Handle /join route
    """
    return render_template('home.html', the_title='BES Courses')

@app.route('/login_ld')
def ld_login_page() -> 'str':
    """
    Handle login page for LN Dev course
    """
    return render_template('login_ld.html', the_title='BES Login')

@app.route('/login_besd')
def besd_login_page() -> 'str':
    """
    Handle login page for Bitcoin Dev course
    """
    return render_template('login_besd.html', the_title='BES Login')

@app.route('/login_besd_c2_l')
def besd_login_c2_page() -> 'str':
    """
    Handle Chapter 2 of Bitcoin dev course route
    """
    return render_template('besd_c2.html', the_title='Bitcoin Dev Course')

@app.route('/login_ld_c2')
def ld_login_c2_page() -> 'str':
    """
    Handle Chapter 2 of LN Dev course route
    """
    return render_template('ld_c2.html', the_title='Lightning Dev Course')


@app.route('/login_besd_result', methods=['POST'])
def besd_login_page_result() -> 'str':
    """
    Handle Login on Bitcoin Dev Course Check
    """
    json_file = "file.json"
    email = request.form['mail']
    password = request.form['password']

    with open(json_file) as file:
        data = json.load(file)

    for user, user_data in data.items():
        if 'email' in user_data and 'password' in user_data:
            if user_data['email'] == email and user_data['password'] == password:
                return render_template('besd.html', the_title='Bitcoin Dev Course')
            else:
                continue
    return render_template('erreur_page.html', the_title='Login Error')


@app.route('/login_ld_result', methods=['POST'])
def ld_login_page_result() -> 'str':
    """
    Handle Login on LN Dev Course Check
    """
    json_file = "file.json"
    email = request.form['mail']
    password = request.form['password']

    with open(json_file) as file:
        data = json.load(file)

    for user, user_data in data.items():
        if 'email' in user_data and 'password' in user_data:
            if user_data['email'] == email and user_data['password'] == password:
                return render_template('ld.html', the_title='Lightning Dev Course')
            else:
                continue
    return render_template('erreur_page.html', the_title='Login Error')


@app.route('/login_result', methods=['POST'])
def login_result_page() -> 'str':
    """
    Handle Login sessions
    """
    json_file = "file.json"
    email = request.form['mail']
    password = request.form['password']

    with open(json_file) as file:
        data = json.load(file)
    courses = []
    for user_id, user_data in data.items():
        if 'email' in user_data and user_data['email'] == email:
            if 'courses' in user_data:
                courses = user_data['courses']
    categories = []
    for user_id, user_data in data.items():
        if 'email' in user_data and user_data['email'] == email:
            if 'categories' in user_data:
                categories = user_data['categories']
    for user, user_data in data.items():
        if 'email' in user_data and 'password' in user_data:
            if user_data['email'] == email and user_data['password'] == password:
                return render_template('login_result.html', the_title='Welcome on BES', the_mail=email, the_password=password)

    return render_template('login_result.html', the_title='Welcome on BES', the_courses=courses, the_categories=categories )


@app.route('/service/<service_id>')
def service_page(service_id):
    """
    Return a specific service page
    """
    return render_template('service_page.html', service_data=service_data)

@app.route('/bitcoin.pdf')
def serve_whitepaper():
    """
    Handle /bitcoin.pdf and serve Bitcoin Whitepaper
    """
    return send_from_directory('static/files', 'bitcoin.pdf')

@app.teardown_appcontext
def close_app(exception):
    """
    Handle Closing App
    """
    print("Closing")

@app.errorhandler(404)
def not_found(error):
    """
    Handle error 404
    """
    return make_response(jsonify({"error": "empty, like shitcoins"}), 404)

if __name__ == "__main__":
    """
    Run the main app with specified HOST and PORT
    """
    HOST = getenv('BES_API_HOST', '127.0.0.1')
    PORT = getenv('BES_API_PORT', 5000)
    app.run(host=HOST, port=PORT, debug=True, threaded=True)
