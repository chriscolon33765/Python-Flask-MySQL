
import imp
from flask import render_template,redirect,request

from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author


@app.route("/add_book")
def add_book():
    books = Book.get_all()
    return render_template("add_book.html", all_books = books)


@app.route("/create/book", methods=["POST"])
def create_book():
    Book.save(request.form)
    return redirect("/add_book")

@app.route("/book/<int:id>")
def show_book(id):
    data = {
    "id" : id
    }
    return render_template("show_book.html" , book=Book.get_by_id(data), unfavorited_authors=Author.unfavorited_authors(data))