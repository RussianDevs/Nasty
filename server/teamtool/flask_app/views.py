from flask import flash, make_response, redirect, render_template, request, url_for
from flask_login import login_required, current_user, login_user, logout_user


from .app import app, db
from .forms import *
from .models import *


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/login/', methods=['get', 'post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        flash('Неверное имя пользователя или пароль', 'error')
        return redirect(url_for('login'))
    if request.method == 'POST':
        if form.show_password.data:
            form.password.type = 'StringField'
    return render_template('login.html', form=form)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из акаунта', 'message')
    return redirect(url_for('login'))
