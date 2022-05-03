
from flask import render_template,redirect,request

from flask_app import app

from flask_app.models import dojo, ninja

@app.route("/new_ninja")
def ninjas():
    return render_template("new_ninja.html", dojos = dojo.Dojo.get_all())

@app.route("/create/new_ninja", methods=["POST"])
def new_ninja():
    ninja.Ninja.save(request.form)
    return redirect("/")
