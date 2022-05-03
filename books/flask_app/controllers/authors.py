from flask import render_template,redirect,request

from flask_app import app

from flask_app.models.author import Author

@app.route("/")
def index():
    authors = Author.get_all()
    return render_template("index.html", all_authors = authors)

@app.route("/author")
def author():
    return render_template("author.html")

@app.route("/create/author", methods=["POST"])
def create_author():
    Author.save(request.form)
    return redirect("/")

@app.route("/author/<int:id>")
def show_author(id):
    data = {
        "id" : id
    }
    return render_template("author.html", author = Author.get_one_with_authors(data))