from flask import make_response, jsonify
from flask_login import login_required, current_user
from flask_restful import Resource

class AccountInfo(Resource):
    decorators = [login_required]

    def get(self):
        return make_response(jsonify({"firstname": current_user.firstname, "lastname": current_user.lastname, "post": current_user.post.name}))
    