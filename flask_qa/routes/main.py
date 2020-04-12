from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from flask_qa.extensions import db
from flask_qa.models import doctors, patients

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        doctor = doctors.query.filter_by(username=name).first()

        error_message = ''

        if not doctor or not check_password_hash(doctor.password, password):
            error_message = 'Could not login. Please try again or register.'
            flash(error_message)
            return redirect(url_for('main.login'))

        if not error_message:
            login_user(doctor)
            return redirect(url_for('main.home'))

    return render_template('login.html')

@main.route('/registerdoctor', methods=['GET', 'POST'])
def registerdoctor():
    if request.method == 'POST':
        name = request.form['name']
        unhashed_password = request.form['password']

        doctor = doctors.query.filter_by(username=name).first()

        if not doctor:
            doctor = doctors(
                username=name,
                unhashed_password=unhashed_password,
            )
        else: 
            flash('User already registered. Login please.')
            return redirect(url_for('main.registerdoctor'))

        db.session.add(doctor)
        db.session.commit()
        return redirect(url_for('main.login'))

    return render_template('registerdoctor.html')

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')

@main.route('/registerpatient', methods=['GET', 'POST'])
def registerpatient():
    if request.method == 'POST':
        name_first = request.form['name_first']
        name_last = request.form['name_last']
        dob = request.form['dob']
        email = request.form['email']
        address = request.form['address']
        phone = request.form['phone']

        patient = patients.query\
        .filter_by(email=email)\
        .filter_by(name_first=name_first)\
        .filter_by(name_last=name_last)\
        .first()
        reg_error = ''

        if not patient:
            patient = patients(
                name_first=name_first,
                name_last=name_last,
                dob=dob,
                email=email,
                address=address,
                phone=phone,
                )

        db.session.add(patient)
        db.session.commit()

        if not reg_error:
            reg_error = 'Patient has already been registered. Please return the device.'
            flash(reg_error)
            return redirect(url_for('main.registerpatient')) 

        flash("Patient successfully registered! Please return the device.")
        return redirect(url_for('main.registerpatient'))

    return render_template('registerpatient.html')

@main.route('/patientsearch', methods=['GET', 'POST'])
@login_required
def patientsearch():
    return render_template('patientsearch.html')

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
