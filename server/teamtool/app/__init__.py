from flask import Flask
from flask_babel import Babel, lazy_gettext as _l
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy

app = Flask("NastyServer")
app.config.from_object("config")

bootstrap = Bootstrap(app)

babel = Babel(app)

db = SQLAlchemy(app)

migrations = Migrate(app, db)


login_manager = LoginManager(app)
login_manager.login_message =_l( 'Please log in to get access to this content.')
login_manager.login_message_category = 'error'
login_manager.login_view = 'frontend.login'

nav = Nav(app)

from .api import bp as api_bp
from . import views
from . import utils

app.register_blueprint(api_bp, url_prefix="/api")

