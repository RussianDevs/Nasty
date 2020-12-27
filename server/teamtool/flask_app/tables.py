fro flask_babel import lazy_gettext as _l
from flask_table import Table, Col


class UsersTable(Table):
    id = Col(_l("Id"))
    username = Col(_l("Username"))
    firstname = Col(_l("Firstname"))
    lastname = Col(_l("Lastname"))
    email = Col(_l("Email"))
    password_hash = Col(_l("Password hash"))
    permission = Col(_l("Permission"))
