from .. import restful_api
from . import information

restful_api.add_resource(information.AccountInfo, "/api/account/info", endpoint="account_information")

