
from flask import flash, render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.controllers.users import User
from flask_app import app


@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    print(request.form)
    if "user_id" not in session:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        return redirect("/new")
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "under_30" : int(request.form["under_30"]),
        "date_made" : request.form["date_made"],
        "user_id" : session["user_id"]
    }
    Recipe.save(data)
    return redirect("/dashboard")

@app.route("/edit/recipes/<int:id>")
def edit(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id":id
    }
    user_data = {
        "id": session["user_id"]
    }
    return render_template("edit_recipe.html", edit = Recipe.get_one(data), user = User.get_by_id(user_data))

@app.route("/update/recipes/<int:id>", methods=["POST"])
def update_recipe(id):
    print(request.form)
    if "user_id" not in session:
        return redirect("/logout")
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/edit/recipes/{id}")
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "under_30" : int(request.form["under_30"]),
        "date_made" : request.form["date_made"],
        "id" : request.form["id"]
    }
    Recipe.update(data)
    return redirect("/dashboard")

@app.route("/recipes/show/<int:id>")
def show(id):
    if "user_id" not in session:
        return redirect("/logout")
    data ={
        "id":id
    }
    user_data = {
        "id": session["user_id"]
    }
    return render_template("show_painting.html", recipe = Recipe.get_one(data), user = User.get_by_id(user_data))

@app.route("/destroy/recipes/<int:id>")
def destroy_recipe(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id" : id
    }
    Recipe.destroy(data)
    return redirect("/dashboard")
