import os

app_dir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'MAYu17042006|8b/172'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app_dir, "sqlite.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False



DEBUG = False

LANGUAGES = ['ru', 'en']

