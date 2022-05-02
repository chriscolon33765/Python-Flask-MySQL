
from flask import flash, render_template, redirect, request, session
from flask_app.models.register import Register
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register_user():
    if not Register.validate_user(request.form):
            return redirect("/")
    data = {
            "first_name" : request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"],
            "password" : bcrypt.generate_password_hash(request.form['password'])
        }
    session["user_id"] = Register.create(data)
    return redirect ("/dashboard")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    return render_template("/dashboard.html", user = Register.get_one({"id": session['user_id']}))


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# @app.route("/login", methods=["POST"])
# def login():
#     user_from_db = Register.get_by_email({"email":request.form["email"]})
#     if user_from_db and bcrypt.check_password_hash(user_from_db.password, request.form["password"]):
#         session["user_id"] = user_from_db.id
#         return redirect("/dashboard.html")
#     else:
#         flash("Invalid email/password", "login")
#         return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    user = Register.get_by_email(request.form)

    if not user:
        flash("Invalid email/password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid email/password", "login")
        return redirect("/")
    session["user_id"] = user.id
    return redirect("/dashboard")
