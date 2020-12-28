from flask import url_for, make_response, jsonify
from flask_login import login_required, current_user, login_user
from flask_restful import Resource

from app import db

from app.models import User



class Organization(Resource):
    decorators = [login_required]

    def get(self):
        return "name", 200


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

