from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from flask_qa.extensions import db
from flask_qa.models import Doctors

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        doctor = Doctors.query.filter_by(username=name).first()

        error_message = ''

        if not doctor or not check_password_hash(doctor.password, password):
            error_message = 'Could not login. Please try again or register.'
            flash(error_message)
            return redirect(url_for('main.login'))

        if not error_message:
            login_user(doctor)
            return redirect(url_for('main.home'))

    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        unhashed_password = request.form['password']

        doctor = Doctors(
            username=name, 
            unhashed_password=unhashed_password,
        )

        db.session.add(doctor)
        db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')

@main.route('/patients', methods=['GET', 'POST'])
@login_required
def patients():
    return render_template('patients.html')

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))