from flask import render_template, request
from flask_login import current_user, login_required

from app import app, db
from app.models import User
from app.tables import get_user_profile_table

@app.route("/account/profile/", endpoint="frontend.account.profile")
@app.route("/account/profile/<int:id>/", endpoint="frontend.account.profile")
def account(id=0):
    if id != 0:
        user = db.session.query(User).get(id)
        if user:
            return render_template("account/profile.html", user=user, user_profile_table=get_user_profile_table(user))
        else:
            return render_template("errors/404.html"), 404
    else:
        if current_user.is_authenticated:
            return render_template("account/profile.html", user=current_user, user_profile_table=get_user_profile_table(current_user))
        else:
            return render_template("errors/401.html"), 401            
