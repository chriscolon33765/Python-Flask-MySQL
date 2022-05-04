

from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User




@app.route("/users")
def index():
    users = User.get_all_users()
    return render_template("users.html", users = users)


@app.route("/users/new")
def new():
    return render_template("new.html")


@app.route("/users/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/users")

@app.route("/users/edit/<int:id>")
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit_user.html", user = User.get_one(data))

@app.route("/users/show/<int:id>")
def show(id):
    data ={
        "id":id
    }
    return render_template("show_user.html", user = User.get_one(data))

@app.route("/users/update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/users")


@app.route("/users/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/users")