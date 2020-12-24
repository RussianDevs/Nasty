from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from .app import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    mail = db.Column(db.String(128))
    permission = db.Column(db.BigInteger())
    password_hash = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
