from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255))
    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64))
    permission_id = db.Column(db. BigInteger())
    users = db.relationship('User', backref='post')

    def __str__(self):
        return self.name

    def get_permissions(self):
        results = []
        permission_id = self.permission_id
        for i in range(32,0,-1):
            if permission_id - 2 ** i > 0:
                results.append(i)
        return reversed(results)

