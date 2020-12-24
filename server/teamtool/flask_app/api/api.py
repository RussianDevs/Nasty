from flask import url_for, make_response, jsonify
from flask_login import login_required, current_user, login_user
from flask_restful import Resource

from ..app import app, db

from ..models import User



class Organization(Resource):
    decorators = [login_required]

    def get(self):
        return "name", 200


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

class Registration(Resource):
    # decorators = [login_required]

    def post(self, username, firstname, lastname, password, mail, permission):
        user = User()
        user.username = username
        user.firstname = firstname
        user.lastname = lastname
        user.set_password(password)
        user.mail = mail
        user.permission = permission
        db.session.add(user)
        db.session.commit()

class AccountDescription(Resource):
    decorators = [login_required]

    def get(self):
        return make_response(jsonify({"firstname": current_user.firstname, "lastname": current_user.lastname, "permission": current_user.permission}))
