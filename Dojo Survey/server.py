

from flask import Flask, render_template,request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "This is a secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():
    session["name"] = request.form["name"]
    session["city"] = request.form["city"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    session["checkbox"] = request.form["checkbox"]
    session["radiobutton"] = request.form["radiobutton"]

    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html")





if __name__ == "__main__":
    app.run(debug=True)