from flask import request
from flask_babel import _, lazy_gettext as _l
from flask_login import current_user
from flask_nav.elements import Navbar, View, Link, Text, Subgroup, NavigationItem

from app import app, babel, nav

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

class GreetingText(Text):
    @property
    def Text(self):
        return _("Welcome {} {}").format(current_user.firstname, current_user.lastname)


gen_navbar = Navbar(
    "Nasty teamtool",
    GreetingText("Hi"),
    View(_l("Home"), "frontend.index"),
)

nav.register_element("gen", gen_navbar)

usr_navbar = Navbar(
    View(_l("My profile"), "frontend.account.profile"),
)

nav.register_element("usr", usr_navbar)
