from flask import request
from flask_babel import _, lazy_gettext as _l
from flask_login import current_user
from flask_nav.elements import Navbar, View, Link, Text, Subgroup

from app import app, babel, nav

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

class GreetingText(Text):
    def __init__(self):
        pass

    @property
    def text(self):
        print("a")
        if current_user.is_authenticated():
            print("m1")
            return _("Welcome {} {}").format(current_user.firstname, current_user.lastname)
        else:
            print("m2")
            return _("Welcome")


gen_navbar = Navbar(
    # GreetingText(),
    View(_l("Home"), "frontend.index"),
)

nav.register_element("gen", gen_navbar)

usr_navbar = Navbar(
    View(_l("My profile"), "frontend.account.profile"),
)

nav.register_element("usr", usr_navbar)
