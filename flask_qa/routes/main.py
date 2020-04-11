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
        reg_error = ''

        if not doctor:
            doctor = doctors(
                username=name,
                unhashed_password=unhashed_password,
            )

        db.session.add(doctor)
        db.session.commit()
        return redirect(url_for('main.login'))


        if not reg_error:
            reg_error = 'User already registered. Login please.'
            flash(reg_error)
            return redirect(url_for('main.registerdoctor'))

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

        flash("Patient successfully registered! Please return the device.")


        return redirect(url_for('main.registerpatient'))

    return render_template('registerpatient.html')

@main.route('/patients', methods=['GET', 'POST'])
@login_required
def patients():
    return render_template('patients.html')

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
