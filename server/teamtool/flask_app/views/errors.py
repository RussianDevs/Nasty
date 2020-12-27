from flask import render_template

from ..app import app

@app.errorhandler(404)
def error404(error):
    return render_template("errors/404.html", error=error), 404
