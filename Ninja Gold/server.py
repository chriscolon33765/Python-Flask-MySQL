

from flask import Flask, render_template, redirect, request, session
import random
import datetime
app = Flask(__name__)
app.secret_key="This is a secret"



@app.route("/")
def index():
    if "total_gold" and "activities" not in session:
        session["total_gold"] = 0
        session["activities"] = ""

    return render_template("index.html", messages=session["activities"])

@app.route("/process_money", methods = ["POST"])
def process_money():
    todays_time = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
    location = request.form["building"]
    if location == "farm":
        my_gold = random.randint(10,20)
    elif location == "cave":
        my_gold = random.randint(5,10)
    elif  location == "house":
        my_gold = random.randint(2,5)
    else:
        my_gold = random.randint(-50,50)
    session["total_gold"] += my_gold

    if my_gold >= 0:
        new_message = f"<p style='color: green'>Awesome! You won {my_gold} gold pieces from the {location} {todays_time}</p>"
        session["activities"] += new_message
    elif my_gold < 0:
        new_message = f"<p style='color: red'>Sorry, you lost {my_gold} gold pieces from the {location} {todays_time}</p>"
        session["activities"] += new_message
    return redirect("/")



@app.route("/reset")
def reset_gold():
    session.clear()

    return redirect("/")










if __name__ == ("__main__"):
    app.run(debug=True)