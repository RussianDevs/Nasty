from flask import abort, request, render_template

from app import app, db


@app.errorhandler(401)
def error401(error):
    return render_template("errors/401.html", error=error), 401

@app.errorhandler(403)
def error403(error):
    return render_template("errors/403.html", error=error), 403

@app.errorhandler(404)
def error404(error):
    return render_template("errors/404.html", error=error, path=request.path), 404

@app.errorhandler(405)
def error405(error):
    return render_template("errors/405.html", error=error), 405

@app.errorhandler(500)
def error500(error):
    db.session.rollback()
    return render_template("errors/500.html", error=error), 500

@app.route("/generate_error/<int:error_code>/")
def generate_error(error_code):
    abort(error_code)

