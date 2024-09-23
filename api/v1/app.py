"""
Main Module of our application
"""
from api.v1.views import app_views
from flask import Flask, make_response, jsonify, render_template, request, send_from_directory, session
from os import getenv
import json
import requests

app = Flask(__name__)

# app.secret_key = '12345'
app.config.from_pyfile('BES_CONFIG.py')
app.register_blueprint(app_views)

@app.route('/')
def bes() -> str:
    """
    Handles / route and return Homepage
    """
    return render_template('home.html', the_title='Bitcoin Engineering School')

@app.route('/courses')
def index() -> str:
    """
    Handle /join route
    """
    return render_template('courses.html', the_title='BES Courses')

@app.route('/login')
def ld_login_page() -> 'str':
    """
    Handle login page for LN Dev course
    """
    return render_template('login.html', the_title='BES Login')

@app.route('/lnbcp')
def lnbcp() -> str:
    """
    Chapter 1 lnbcp
    """
    if session['loggedin'] == True:
        return render_template('lnbcp.html', the_title='LN Bootcamp')
    else:
        return render_template('login.html', the_title='Login BES')

@app.route('/lnbcp2')
def lnbcp2() -> str:
    """
    Chapter 2 lnbcp
    """
    if session['loggedin'] == True:
        return render_template('lnbcp2.html', the_title='LN Bootcamp')
    else:
        return render_template('login.html', the_title='Login BES')

@app.route('/lnbcp3')
def lnbcp3() -> str:
    """
    Chapter 3 lnbcp
    """
    return render_template('lnbcp3.html', the_title='LN Bootcamp')

@app.route('/lnbcp4')
def lnbcp4() -> str:
    """
    Chapter 4 lnbcp
    """
    return render_template('lnbcp4.html', the_title='LN Bootcamp')

@app.route('/bitdev')
def bitdev() -> str:
    """
    Chapter 1 bitdev
    """
    return render_template('bitdev.html', the_title='Bitdev Course')

@app.route('/bitdev2')
def bitdev2() -> str:
    """
    Chapter 2 bitdev
    """
    return render_template('bitdev2.html', the_title='Bitdev Course')

@app.route('/lndev')
def lndev() -> str:
    """
    Chapter 1 lndev
    """
    return render_template('lndev.html', the_title='Lndev Course')

@app.route('/lndev2')
def lndev2() -> str:
    """
    Chapter 2 lndev
    """
    return render_template('lndev2.html', the_title='Lndev Course')

@app.route('/loginres', methods=['POST'])
def loginres() -> str:
    """
    Handle Login Check
    """
    json_file = "file.json"
    email = request.form['mail']
    password = request.form['password']

    with open(json_file) as file:
        data = json.load(file)

    for user, user_data in data.items():
        if 'email' in user_data and 'password' in user_data:
            if user_data['email'] == email and user_data['password'] == password:
                session['loggedin'] = True
                session['id'] = user_data['id']
                session['username'] = user_data['username']
                session['git_username'] = user_data['git_username']
                return render_template('courses.html', the_title='BES Courses')
            else:
                continue
    return render_template('loginerror.html', the_title='Login Error')

@app.route('/signup', methods=['GET'])
def signup():
    """
    Handle signup
    """
    return render_template('signup.html', the_title="BES Signup")

@app.route('/signupres', methods=['POST'])
def signupres():
    """
    Handle sigup check
    """
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    git_username = request.form['git_username']

    data = {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'email': email,
        'password': password,
        'git_username': git_username
    }

    response = requests.post('http://bes.alphonsemehounme.tech/api/v1/users', json=data)

    if response.status_code == 201:
        return render_template('login.html', the_title='BES Login')
    else:
        return render_template('signup.html', the_title='BES Signup')


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
    PORT = getenv('BES_API_PORT', 8000)
    app.run(host=HOST, port=PORT, debug=True, threaded=True)
