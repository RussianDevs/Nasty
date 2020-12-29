from flask import Blueprint
from flask_restful import Api
from flask_httpauth import HTTPTokenAuth


bp = Blueprint("api", __name__)

token_auth = HTTPTokenAuth(bp)

restful_api = Api(bp, prefix="/v1")

'''from app.api.api import Organization, Login, Registration, AccountDescription
restful_api.add_resource(Organization, "/organization", endpoint="api.organization")   
restful_api.add_resource(Registration, "/api/registration", "/api/registration/<string:username>/<string:firstname>/<string:lastname>/<string:password>/<string:mail>/<int:permission>", endpoint="registration")
# restful_api.add_resource(AccountDescription, "/api/account/get-info", endpoint="get-account-info")'''

#from app.api import account
from app.api import login

restful_api.add_resource(login.Login, '/login', '/login/<string:username>/<string:password>', endpoint="api_login")

