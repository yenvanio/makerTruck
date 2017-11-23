from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy(app)

class Workshops (db.Model):
    __tablename__ = "workshops"
    id = db.Column('id', db.Integer, primary_key=True)
    price = db.Column('price', db.Float)
    name = db.Column('name', db.Unicode)

class Bins (db.Model):
    __tablename__ = "bins"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    workshop_id = db.Column('workshop_id', db.Integer, db.ForeignKey('workshops.id'))
    quantity = db.Column('quantity', db.Integer)

    workshops = db.relationship('Workshops', foreign_keys=workshop_id)

class School (db.Model):
    __tablename__ = "school"
    id = db.Column('id', db.Integer, primary_key=True)
    address = db.Column('address', db.Unicode)
    school_name = db.Column('school_name', db.Unicode)
    email = db.Column('email', db.Unicode)
    phone = db.Column('phone', db.Integer)
    username = db.Column('username', db.Unicode)
    password = db.Column('password', db.Unicode)

class Trucks (db.Model):
    __tablename__ = "trucks"
    id = db.Column('id', db.Integer, primary_key=True)
    model = db.Column('model', db.Unicode)
    VIN = db.Column('VIN', db.Unicode)
    license_plate = db.Column('license_plate', db.Unicode)


class WorkshopBooking (db.Model):
    __tablename__ = "workshop_booking"
    id = db.Column('id', db.Integer, primary_key=True)
    workshop_id = db.Column('workshop_id', db.Integer, db.ForeignKey('workshops.id'))
    school_id = db.Column('school_id', db.Integer, db.ForeignKey('school.id'))
    truck_id = db.Column('truck_id', db.Integer, db.ForeignKey('trucks.id'))
    date = db.Column('date', db.Integer)
    type = db.Column('type', db.Unicode)
    period = db.Column('period', db.Integer)

    workshops = db.relationship('Workshops', foreign_keys=workshop_id)
    schools = db.relationship('School', foreign_keys=school_id)
    trucks = db.relationship('Trucks', foreign_keys=truck_id)
