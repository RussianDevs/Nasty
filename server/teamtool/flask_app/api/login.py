from flask_login import current_user, login_user
from flask_restful import Resource

from ..app import db
from ..models import User


class Login(Resource):
    def get(self):
        if current_user.is_authenticated:
           return  "Uou are authenticated.", 403
        else:
            return "Sory, You haven\'t access to our service", 401

    def post(self, username, password):
        user = db.session.query(User).filter(User.username == username).first()
        if user and user.check_password(password):
            login_user(user)
        else:
            return "Invalid username or password"

