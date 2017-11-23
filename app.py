from flask import Flask, render_template, redirect, jsonify, url_for, request, session
from flask_restful import Api
from flask_wtf import Form
from flask_wtf.csrf import CsrfProtect
from wtforms import SelectField
from db import helper as connection
from db.models import Workshops

# initalize server
app = Flask(__name__, template_folder='views', static_folder='public')
api = Api(app)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CsrfProtect(app)

# create connection object and get data for teams and players
db = connection.Connection()

@app.route('/', methods=['GET'])
def index():
    workshops = db.get_workshops()
    return render_template("index.html", workshops=workshops)

@app.route('/workshops', methods=['GET'])
def workshops():
    workshops1 = db.get_availWorkshops()
    workshops2 = db.get_unavailWorkshops()
    return render_template("workshops.html", available=workshops1, unavailable=workshops2)

@app.route('/bins', methods=['GET'])
def bins():
    bins1 = db.get_availBins()
    bins2 = db.get_unavailBins()
    return render_template("bins.html", available=bins1, unavailable=bins2)


@app.route('/trucks', methods=['GET'])
def trucks():
    trucks1 = db.get_availTrucks()
    trucks2 = db.get_unavailTrucks()
    return render_template("trucks.html", available=trucks1, unavailable=trucks2)

@app.route('/schools', methods=['GET'])
def schools():
    schools = db.get_schools()
    return render_template("schools.html", schools=schools)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
