from flask import render_template,redirect,request

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

@app.route("/new_ninja")
def new_dojo():
    return render_template("new_ninja.html")

@app.route("/dojo")
def dojo():
    return render_template("dojo.html")

@app.route("/create/dojo", methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect("/")


@app.route("/dojo/<int:id>")
def show_dojo(id):
    data = {
        "id" : id
    }
    return render_template("dojo.html", dojo = Dojo.get_one_with_ninjas(data))




