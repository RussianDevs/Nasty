from flask_babel import lazy_gettext as _l
from flask_table import Table, Col


class UserProfileTable(Table):
    username = Col(_l("Username"))
    firstname = Col(_l("Firstname"))
    lastname = Col(_l("Lastname"))
    email = Col(_l("Email"))
    post = Col(_l("Post"))

def get_user_profile_table(u):
    return UserProfileTable([{"username": u.username, "firstname": u.firstname, "lastname": u.lastname, "email": u.email, "post": u.post},])
