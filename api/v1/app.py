from api.v1.views import app_views
from flask import Flask, make_response, jsonify, render_template, request
from os import getenv
import json

app = Flask(__name__)
app.register_blueprint(app_views)

@app.route('/')
def index() -> str:
    return render_template('home.html', the_title='welcome on BES')

@app.route('/login_ld')
def ld_login_page() -> 'str':
    return render_template('login_ld.html', the_title='Please log on ls')

@app.route('/login_besd')
def besd_login_page() -> 'str':
    return render_template('login_besd.html', the_title='Please log on besd')

@app.route('/login_besd_c2_l')
def besd_login_c2_page() -> 'str':
    return render_template('besd_c2.html', the_title='Please log on besd chapter 2')

@app.route('/login_ld_c2')
def ld_login_c2_page() -> 'str':
    return render_template('ld_c2.html', the_title='Please log on ls chapter 2')


@app.route('/login_besd_result', methods=['POST'])
def besd_login_page_result() -> 'str':
    json_file = "file.json"
    email = request.form['mail']
    password = request.form['password']

    with open(json_file) as file:
        data = json.load(file)

    for user, user_data in data.items():
        if 'email' in user_data and 'password' in user_data:
            if user_data['email'] == email and user_data['password'] == password:
                return render_template('besd.html', the_title='Welcome on BES')
            else:
                return render_template('erreur_page.html', the_title='You not not the person')

@app.route('/login_ld_result', methods=['POST'])
def ld_login_page_result() -> 'str':
    json_file = "file.json"
    email = request.form['mail']
    password = request.form['password']

    with open(json_file) as file:
        data = json.load(file)

    for user, user_data in data.items():
        if 'email' in user_data and 'password' in user_data:
            if user_data['email'] == email and user_data['password'] == password:
                return render_template('ld.html', the_title='Welcome on BES')
            else:
                return render_template('erreur_page.html', the_title='You not not the person')



@app.route('/login_result', methods=['POST'])
def login_result_page() -> 'str':

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
    # Récupérer les données associées à la carte à partir de la base de données ou de toute autre source
    # Utilisez service_id pour identifier la carte cliquée
    # Par exemple, récupérez le titre, la description, les images, etc.

    # Renvoyer les données à la page de service
    return render_template('service_page.html', service_data=service_data)

@app.teardown_appcontext
def close_app(exception):
    print("Closing")

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "empty, like shitcoins"}), 404)

if __name__ == "__main__":
    HOST = getenv('BES_API_HOST', '127.0.0.1')
    PORT = getenv('BES_API_PORT', 5000)
    app.run(host=HOST, port=PORT, debug=True, threaded=True)
