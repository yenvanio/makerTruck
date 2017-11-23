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
    workshops = db.get_workshopsAll()
    return render_template("index.html", workshops=workshops)

@app.route('/workshops', methods=['GET'])
def workshops():
    workshops1 = db.get_availWorkshops()
    workshops2 = db.get_unavailWorkshops()
    return render_template("workshops.html", available=workshops1, unavailable=workshops2)

@app.route('/workshop/<id>', methods=['GET'])
def workshopID(id):
    school_id = id
    workshops = db.get_workshops(school_id)
    school_name = db.get_schoolName(school_id)
    return render_template("workshop.html", workshops=workshops, school_name=school_name)

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

@app.route('/stats', methods=['GET'])
def stats():
    schools1 = db.get_aboveAvgPrice()
    schools2 = db.get_noBookSchool()
    schools3 = db.get_bookSchool()
    return render_template("stats.html", schoolsPrice=schools1, schoolsNoBook=schools2, schoolsBook=schools3)

@app.route('/bookBins/<id>', methods=['GET'])
def bookBins(id):
    truck_id = id
    bookBins = db.get_bookBins(truck_id)
    return render_template("bookBins.html", bookBins=bookBins)



@app.route('/api/workshops/<id>', methods=['GET'])
def workshopAPI(id):
    workshop_id = id
    workshop = db.get_workshop(workshop_id)
    return jsonify(workshop)

@app.route('/api/trucks/<id>', methods=['GET'])
def truckAPI(id):
    truck_id = id
    truck = db.get_truck(truck_id)
    return jsonify(truck)



if __name__ == '__main__':
    app.run(debug=True, host='localhost')
