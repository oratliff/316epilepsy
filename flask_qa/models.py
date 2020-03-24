from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db
from datetime import datetime

class Doctor(UserMixin, db.Model):
    __tablename__ = 'doctors'
    doctorid = db.Column('doctor_id',
                        db.Integer(),
                        primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean())

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)

class Patients(db.Model):
    __tablename__ = 'patients'
    patientid = db.Column('patient_id',
                        db.Integer(),
                        primary_key=True)
    name_first = db.Column('name_first', db.String(20))
    name_last = db.Column('name_last', db.String(20))
    dob = db.Column('dob', db.DateTime)                       #TODO: check if this data type throws errors for handling dates
    sex = db.Column('sex', db.String(6))
    phone = db.Column('phone', db.Integer())
    email = db.Column('email', db.String(50))
    address = db.Column('address', db.String(50))
    visits = db.relationship('Visits', backref = 'Patients')    #one to many rlationship: visits is a list

class Visits(db.Model):
    __tablename__= 'visits'
    visitid = db.Column('visitid', db.Integer(),
                                primary_key=True)
    patientid = db.relationship('patients',
                                db.ForeignKey('patientid'),     #TODO: Check if this needs to reference the db var (patient_id) or the python object (patientid)
                                uselist = False)                #one to one relationship, that's why we've set uselist to False
    doctorid = db.relationship('doctors',
                                db.ForeignKey('doctorid'),
                                uselist = False)                #one to one relationship
    date = db.Column('visit_date', db.DateTime)               #TODO: change this Date datatype if needed from above TODO
    weight = db.Column('weight', db.Float())
    height = db.Column('height', db.Float())
    patient_history = db.Column('patient_history', db.String(500))
    symptoms = db.Column('symptoms', db.String(250))
    diagnostics = db.Column('diagnostics', db.String(250))
    comorbidities = db.Column('comorbidities', db.String(100))
    previous_treatment = db.Column('previous_treatment', db.String(250))
    current_treatment = db.Column('current_treatment', db.String(250))
    current_medications = (db.Column('current_medications', db.String(250)))         #TODO: figure out how to deal with this and the following two medications attribute as a comma separated lists
    current_med_freq = (db.Column('current_med_freq', db.String(20)))
    current_med_dose = (db.Column('current_med_dose', db.String(20)))
