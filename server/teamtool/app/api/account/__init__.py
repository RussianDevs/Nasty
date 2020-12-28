from app.api import restful_api
from app.api.account.information import AccountInfo

restful_api.add_resource(AccountInfo, "/account/info", endpoint="api.account.profile")

