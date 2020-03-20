from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from flask_qa.extensions import db
from flask_qa.models import Question, User

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()

        error_message = ''

        if not user or not check_password_hash(user.password, password):
            error_message = 'Could not login. Please check and try again.'

        if not error_message:
            login_user(user)
            return redirect(url_for('main.home'))

    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        unhashed_password = request.form['password']

        user = User(
            name=name, 
            unhashed_password=unhashed_password,
            admin=False,  
            expert=False
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    # if request.method == 'POST':
    #     question = request.form['question']
    #     expert = request.form['expert']

    #     question = Question(
    #         question=question, 
    #         expert_id=expert, 
    #         asked_by_id=current_user.id
    #     )

    #     db.session.add(question)
    #     db.session.commit()

    #     return redirect(url_for('main.login'))

    # experts = User.query.filter_by(expert=True).all()

    # context = {
    #     'experts' : experts
    # }

    return render_template('home.html')

@main.route('/patients', methods=['GET', 'POST'])
@login_required
def patients():
    # if not current_user.expert:
    #     return redirect(url_for('main.login'))

    # question = Question.query.get_or_404(question_id)

    # if request.method == 'POST':
    #     question.answer = request.form['answer']
    #     db.session.commit()

    #     return redirect(url_for('main.unanswered'))

    # context = {
    #     'question' : question
    # }

    return render_template('patients.html')

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))