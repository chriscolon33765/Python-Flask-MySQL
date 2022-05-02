
from flask import flash, render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    return render_template("dashboard.html", user = User.get_user_with_recipes({"id" : session["user_id"]}), recipes = Recipe.get_all())

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/new")
def new():
    return render_template("/new.html")


@app.route("/register", methods=["POST"])
def register_user():
    if not User.validate_user(request.form):
        return redirect("/")
    data = {
        "f_name" : request.form["f_name"],
        "l_name" : request.form["l_name"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    session["user_id"] = User.create(data)
    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():
    user = User.get_by_email(request.form)

    if not user:
        flash("Invalid username/email", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invlaid Password", "login")
        return redirect("/")
    session["user_id"] = user.id
    return redirect("/dashboard")



