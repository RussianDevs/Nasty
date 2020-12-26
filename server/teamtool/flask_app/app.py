from flask import Flask, request
from flask_babel import Babel, lazy_gettext as _l
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy




app = Flask("NastyServer")
app.config.from_object("config")

bootstrap = Bootstrap(app)

babel = Babel(app)

db = SQLAlchemy(app)

migrations = Migrate(app, db)

restful_api = Api(app)

login_manager = LoginManager(app)
login_manager.login_message =_l( 'Please log in to get access to this content.')
login_manager.login_message_category = 'error'
login_manager.login_view = 'login'

from .import api
from . import views


@babel.localeselector
def get_locale():
    r = request.accept_languages.best_match(app.config['LANGUAGES'])
    print(r)
    return r

navbar = Navbar("top",
    View("Home", "index"),
)

nav = Nav()
nav = Nav()

nav.register_element("top", navbar)

nav.init_app(app)