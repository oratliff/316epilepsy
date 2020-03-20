from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required

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
            return redirect(url_for('main.login'))

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

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

# @main.route('/ask', methods=['GET', 'POST'])
# @login_required
# def ask():
#     if request.method == 'POST':
#         question = request.form['question']
#         expert = request.form['expert']

#         question = Question(
#             question=question, 
#             expert_id=expert, 
#             asked_by_id=current_user.id
#         )

#         db.session.add(question)
#         db.session.commit()

#         return redirect(url_for('main.login'))

#     experts = User.query.filter_by(expert=True).all()

#     context = {
#         'experts' : experts
#     }

#     return render_template('ask.html', **context)

# @main.route('/answer/<int:question_id>', methods=['GET', 'POST'])
# @login_required
# def answer(question_id):
#     if not current_user.expert:
#         return redirect(url_for('main.login'))

#     question = Question.query.get_or_404(question_id)

#     if request.method == 'POST':
#         question.answer = request.form['answer']
#         db.session.commit()

#         return redirect(url_for('main.unanswered'))

#     context = {
#         'question' : question
#     }

#     return render_template('answer.html', **context)

# @main.route('/question/<int:question_id>')
# def question(question_id):
#     question = Question.query.get_or_404(question_id)

#     context = {
#         'question' : question
#     }

#     return render_template('question.html', **context)

# @main.route('/unanswered')
# @login_required
# def unanswered():
#     if not current_user.expert:
#         return redirect(url_for('main.login'))

#     unanswered_questions = Question.query\
#         .filter_by(expert_id=current_user.id)\
#         .filter(Question.answer == None)\
#         .all()

#     context = {
#         'unanswered_questions' : unanswered_questions
#     }

#     return render_template('unanswered.html', **context)

# @main.route('/users')
# @login_required
# def users():
#     if not current_user.admin:
#         return redirect(url_for('main.login'))

#     users = User.query.filter_by(admin=False).all()

#     context = {
#         'users' : users
#     }

#     return render_template('users.html', **context)

# @main.route('/promote/<int:user_id>')
# @login_required
# def promote(user_id):
#     if not current_user.admin:
#         return redirect(url_for('main.login'))

#     user = User.query.get_or_404(user_id)

#     user.expert = True
#     db.session.commit()

#     return redirect(url_for('main.users'))