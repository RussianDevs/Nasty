from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy




app = Flask("NastyServer")
app.config.from_object("config")

db = SQLAlchemy(app)
migrations = Migrate(app, db)
restful_api = Api(app)
login_manager = LoginManager(app)
login_manager.login_message = 'Please enter to get access to this content.'
login_manager.login_message_category = 'error'
login_manager.login_view = 'login'
from .import api