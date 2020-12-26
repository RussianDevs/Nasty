from ..app import restful_api

'''from .api import Organization, Login, Registration, AccountDescription
restful_api.add_resource(Organization, "/api/organization", endpoint="Organization")   
restful_api.add_resource(Registration, "/api/registration", "/api/registration/<string:username>/<string:firstname>/<string:lastname>/<string:password>/<string:mail>/<int:permission>", endpoint="registration")
# restful_api.add_resource(AccountDescription, "/api/account/get-info", endpoint="get-account-info")'''

from . import account
from . import login

restful_api.add_resource(login.Login, '/api/login', '/api/login/<string:username>/<string:password>', endpoint="api_login")
