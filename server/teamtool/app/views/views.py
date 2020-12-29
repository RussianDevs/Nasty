from flask import abort, flash, make_response, redirect, render_template, request, url_for
from flask import abort, flash, make_response, redirect, render_template, request, url_for
from flask_babel import _
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, db
from app.decorators import *
from app.forms import *
from app.models import *


@app.route("/", endpoint="frontend.index")
@app.route("/index", endpoint="frontend.index")
def index():
    return render_template("index.html")

@app.route('/login/', endpoint="frontend.login", methods=['get', 'post'])
def login():
    if current_user.is_authenticated:
        flash(_("You logged in yet"), "info")
        return redirect(url_for('frontend.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('frontend.index')
            return redirect(next_page)
        flash(_("Invalid username or password"), 'error')
        return redirect(url_for('frontend.login'))
    return render_template('login.html', form=form)

@app.route('/logout/', endpoint="frontend.logout")
@login_required
def logout():
    logout_user()
    flash(_("you logged out"), 'info')
    return redirect(url_for('frontend.index'))
