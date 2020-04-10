from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db 

class doctors(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))

    @property
    def unhashed_password(self):
        raise AttributeError('Cannot view unhashed password!')

    @unhashed_password.setter
    def unhashed_password(self, unhashed_password):
        self.password = generate_password_hash(unhashed_password)

class patients(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name_first = db.Column(db.String(50))
    name_last = db.Column(db.String(50))